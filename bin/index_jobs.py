#!/usr/bin/env python3
"""
Index build runner.

Coordinates the corpus index builders so no surface has to wait for one:
builds run in dependency order, in one background thread, and report
progress through src/app/data/index-status.json (read by
GET /api/index/status and the browser chip).

Dependency-safe subsetting: asking for `search` also queues the corpus
builders it reads (asking for `search` queues the corpus builders it reads).
Builders added by a later module (glossarium, qa) register only when their
script exists, so the runner works before and after those corpora land.

Usage:
    python3 bin/index_jobs.py                    # everything, dependency order
    python3 bin/index_jobs.py --only notes,search
    python3 bin/index_jobs.py --status           # last known state, no build
    python3 bin/index_jobs.py --list             # registered builders
    python3 bin/index_jobs.py --background       # detach and return at once

Stdlib only.
"""

import argparse
import importlib
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

from indexlib import REPO, read_status, update_status

# builder -> {module, build kwargs, requires}. Order here is the run order.
BUILDERS = {
    "notes": {"module": "notes_index", "requires": [], "label": "notes corpus"},
    "courses": {"module": "course_index", "requires": [], "label": "courses corpus"},
    "documents": {"module": "document_index", "requires": [], "label": "documents corpus"},
    "library": {
        "module": "build_library_index",
        "requires": ["notes", "courses", "documents"],
        "label": "unified library index",
    },
    "glossarium": {"module": "build_glossarium_index", "requires": [], "label": "glossarium terms"},
    "qa": {"module": "build_qa_index", "requires": [], "label": "Q/A log"},
    "atlas": {"module": "build_technica_atlas", "requires": [], "label": "technica atlas"},
    "search": {
        "module": "build_search_index",
        "requires": ["notes", "courses", "documents", "glossarium", "qa"],
        "label": "universal search snapshot",
    },
}

LOCK = REPO / "src" / "app" / "data" / "index-build.lock"
LOCK_STALE_SECONDS = 6 * 3600
# A lock file is created before its PID is written; give that write time to
# land before treating an unreadable lock as abandoned.
LOCK_WRITE_GRACE_SECONDS = 60

_state_lock = threading.Lock()
_thread = None


# ----------------------------------------------------------------------------
# Registry
# ----------------------------------------------------------------------------

def available() -> list:
    """Registered builders whose script exists, in run order."""
    return [name for name, spec in BUILDERS.items()
            if (REPO / "bin" / (spec["module"] + ".py")).is_file()]


def expand(names) -> list:
    """Add required builders, drop unknown/absent ones, keep run order."""
    have = set(available())
    wanted = set()
    todo = [n for n in names if n in have]
    while todo:
        name = todo.pop()
        if name in wanted:
            continue
        wanted.add(name)
        todo.extend(r for r in BUILDERS[name]["requires"] if r in have)
    return [n for n in BUILDERS if n in wanted]


# ----------------------------------------------------------------------------
# Lock (one build at a time, across processes)
# ----------------------------------------------------------------------------

def _lock_pid():
    """PID recorded in the lock file, or None when it is missing/unreadable."""
    try:
        pid = int(LOCK.read_text(encoding="ascii").strip())
    except (OSError, ValueError):
        return None
    return pid if pid > 0 else None


def _pid_alive(pid: int) -> bool:
    """True when `pid` names a live process."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # The process exists but belongs to another user.
        return True
    return True


def _lock_stale() -> bool:
    """True when the lock is too old or its owning process is gone."""
    try:
        age = time.time() - LOCK.stat().st_mtime
    except OSError:
        return True
    pid = _lock_pid()
    if pid == os.getpid():
        # Our own lock is stale when no build thread is alive.
        with _state_lock:
            return _thread is None or not _thread.is_alive()
    if pid is None:
        # Created but not yet written (or corrupt): allow the writer a moment.
        return age > LOCK_WRITE_GRACE_SECONDS
    if not _pid_alive(pid):
        return True
    return age > LOCK_STALE_SECONDS


def _acquire_lock() -> bool:
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    if LOCK.exists() and _lock_stale():
        try:
            LOCK.unlink()
        except OSError:
            pass
    try:
        fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w") as fh:
        fh.write(str(os.getpid()))
    return True


def _release_lock() -> None:
    # Only remove our own lock: a newer build may have replaced it.
    if _lock_pid() != os.getpid():
        return
    try:
        LOCK.unlink()
    except OSError:
        pass


def busy() -> bool:
    """True when another process (or this one) is already building."""
    with _state_lock:
        if _thread is not None and _thread.is_alive():
            return True
    if not LOCK.exists():
        return False
    return not _lock_stale()


# ----------------------------------------------------------------------------
# Running
# ----------------------------------------------------------------------------

def _run_one(name: str) -> bool:
    spec = BUILDERS[name]
    module = importlib.import_module(spec["module"])
    print("[jobs] %s — %s" % (name, spec["label"]), flush=True)
    progress = _ProgressProxy(name)
    kwargs = {"progress": progress}
    if spec.get("argv") is not None:
        kwargs["argv"] = list(spec["argv"])
    try:
        result = module.build(**kwargs)
    except BaseException as exc:  # noqa: BLE001
        print("[jobs] %s failed: %s: %s" % (name, type(exc).__name__, exc),
              file=sys.stderr, flush=True)
        return False
    return result is not False


class _ProgressProxy:
    """Progress reporter handed to each builder (persists its own entry)."""

    def __init__(self, builder):
        from indexlib import Progress
        self._inner = Progress(builder)
        self.builder = builder

    @property
    def done(self):
        return self._inner.done

    @property
    def total(self):
        return self._inner.total

    def set_total(self, total):
        self._inner.set_total(total)

    def pct(self):
        return self._inner.pct()

    def start(self, message=""):
        self._inner.start(message)

    def stage(self, message):
        self._inner.stage(message)

    def step(self, n=1, message=""):
        self._inner.step(n, message)

    def finish(self, message=""):
        self._inner.finish(message)

    def fail(self, exc):
        self._inner.fail(exc)


def run(names=None, wait=False) -> bool:
    """Start a build; returns False when one is already running."""
    global _thread
    builders = expand(names or available())
    with _state_lock:
        if _thread is not None and _thread.is_alive():
            return False
    if not _acquire_lock():
        return False

    def work():
        try:
            update_status(job={
                "state": "running",
                "builders": builders,
                "started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "finished": None,
                "error": "",
            })
            ok = True
            for name in builders:
                if not _run_one(name):
                    ok = False
                    break
            update_status(job={
                "state": "done" if ok else "error",
                "builders": builders,
                "started": read_status().get("job", {}).get("started"),
                "finished": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "error": "" if ok else "builder failed — see server log",
            }, running=None)
            print("[jobs] %s: %s" % ("done" if ok else "failed", ", ".join(builders)),
                  flush=True)
        finally:
            _release_lock()

    _thread = threading.Thread(target=work, name="index-jobs", daemon=True)
    _thread.start()
    if wait:
        _thread.join()
    return True


def start_background(names=None) -> bool:
    """Detach: run this module in a child process and return immediately."""
    builders = expand(names or available())
    with _state_lock:
        if _thread is not None and _thread.is_alive():
            return False
    if busy():
        return False
    cmd = [sys.executable, str(Path(__file__).resolve()), "--only", ",".join(builders)]
    subprocess.Popen(cmd, cwd=str(REPO),
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     start_new_session=True)
    return True


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def _print_status() -> int:
    state = read_status()
    job = state.get("job") or {}
    job_state = job.get("state") or "idle"
    if job_state == "running" and not busy():
        job_state = "interrupted (no live build)"
    print("job: %s%s" % (job_state,
                         " (%s)" % ", ".join(job.get("builders") or []) if job.get("builders") else ""))
    builders = state.get("builders") or {}
    for name in available():
        entry = builders.get(name)
        if not entry:
            print("  %-10s —" % name)
            continue
        print("  %-10s %-6s %6s/%-6s %5.1f%%  %5.1fs  %s" % (
            name, entry.get("state", "?"), entry.get("done", 0),
            entry.get("total", 0), entry.get("pct", 0.0),
            entry.get("elapsed", 0.0), entry.get("message", "")))
    print("updated: %s" % (state.get("updated") or "—"))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="index_jobs.py",
                                     description="Chunked, progress-reporting index builds.")
    parser.add_argument("--only", help="comma-separated builders (deps are added)")
    parser.add_argument("--status", action="store_true", help="print the last known state")
    parser.add_argument("--list", action="store_true", help="list registered builders")
    parser.add_argument("--background", action="store_true",
                        help="detach into a child process and return at once")
    args = parser.parse_args(argv)

    if args.list:
        for name in available():
            print("%-10s %-32s requires: %s" % (
                name, BUILDERS[name]["label"],
                ", ".join(BUILDERS[name]["requires"]) or "—"))
        return 0
    if args.status:
        return _print_status()

    names = [n.strip() for n in args.only.split(",") if n.strip()] if args.only else None
    if names:
        unknown = [n for n in names if n not in available()]
        if unknown:
            print("unknown builder(s): %s (available: %s)"
                  % (", ".join(unknown), ", ".join(available())), file=sys.stderr)
            return 2

    if args.background:
        return 0 if start_background(names) else 3

    if not run(names, wait=True):
        print("a build is already running — see --status", file=sys.stderr)
        return 3
    job = read_status().get("job") or {}
    return 0 if job.get("state") == "done" else 1


if __name__ == "__main__":
    raise SystemExit(main())
