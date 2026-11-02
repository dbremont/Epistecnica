#!/usr/bin/env python3
"""
Shared index-build plumbing.

Every index builder in bin/ is chunked and progress-aware: it parses the corpus
in chunks, reports `done/total` through a Progress object, and persists that
state to src/app/data/index-status.json so the server (GET /api/index/status)
and the browser chip can show live progress without waiting for the build.

- `Progress` — per-builder progress reporter (chunked flush, elapsed time).
- `atomic_write_text` — write `<out>.tmp` then `os.replace`, so a reader never
  sees a half-written index.
- `read_status` / `status_path` — the persisted state, shared with bin/serve.py.

Builders keep working standalone (`python3 bin/notes_index.py`) and expose a
`build(progress=None)` entry point that bin/index_jobs.py drives.

Stdlib only.
"""

import json
import os
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATUS = REPO / "src" / "app" / "data" / "index-status.json"

# Flush the status file at most this often (seconds) and at least every
# FLUSH_EVERY items, so tiny corpora still show movement.
FLUSH_SECONDS = 0.4
FLUSH_EVERY = 25

_LOCK = threading.Lock()


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def status_path() -> Path:
    return STATUS


def read_status() -> dict:
    """The persisted status map ({updated, running, builders}), never raising."""
    try:
        return json.loads(STATUS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"updated": None, "running": None, "builders": {}}


def atomic_write_text(path: Path, text: str) -> None:
    """Write `text` to `path` atomically (tmp file beside it + os.replace)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _write_state(state: dict) -> None:
    """Atomically persist the whole status map (creating its dir if needed)."""
    state["updated"] = now_iso()
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATUS.with_name(STATUS.name + ".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, separators=(",", ":")),
                   encoding="utf-8")
    os.replace(tmp, STATUS)


def update_status(**fields) -> None:
    """Merge top-level fields into the status map (job state, running flag)."""
    with _LOCK:
        state = read_status()
        state.update(fields)
        _write_state(state)


def _merge(entry: dict) -> None:
    """Read-modify-write one builder entry into the status file."""
    with _LOCK:
        state = read_status()
        builders = state.get("builders") or {}
        builders[entry["builder"]] = entry
        state["builders"] = builders
        state["running"] = entry["builder"] if entry["state"] == "running" else None
        _write_state(state)


class Progress:
    """Chunked progress reporter for one builder.

    Usage:
        progress = Progress("notes")
        progress.set_total(len(files))
        for path in files:
            ...
            progress.step()
        progress.finish("7300 notes")

    A builder run passes `write_status=False` when the caller (index_jobs) owns
    the status entry; the CLI default persists it so a manual build is visible.
    """

    def __init__(self, builder: str, total: int = None, write_status: bool = True,
                 stream=None):
        self.builder = builder
        self.total = total or 0
        self.done = 0
        self.write_status = write_status
        self.stream = stream or sys.stdout
        self.started_at = time.time()
        self._last_flush = 0.0
        self._since_flush = 0
        self._message = ""
        self.state = "idle"

    # -- reporting -----------------------------------------------------

    def set_total(self, total: int) -> None:
        self.total = total

    def pct(self) -> float:
        if not self.total:
            return 0.0
        return round(min(100.0, 100.0 * self.done / self.total), 1)

    def _entry(self, state: str) -> dict:
        return {
            "builder": self.builder,
            "state": state,
            "done": self.done,
            "total": self.total,
            "pct": self.pct(),
            "started": datetime.fromtimestamp(self.started_at).isoformat(timespec="seconds"),
            "elapsed": round(time.time() - self.started_at, 1),
            "message": self._message,
            "error": "",
        }

    def start(self, message: str = "") -> None:
        self.state = "running"
        self._message = message
        self._write(force=True)
        if message:
            self._log(message)

    def stage(self, message: str) -> None:
        """A new phase inside the builder (chunk boundary, layout pass, …)."""
        self._message = message
        self._write(force=True)

    def step(self, n: int = 1, message: str = "") -> None:
        self.done += n
        self._since_flush += 1
        if message:
            self._message = message
        if self._since_flush >= FLUSH_EVERY or (time.time() - self._last_flush) >= FLUSH_SECONDS:
            self._write()

    def finish(self, message: str = "") -> None:
        self.state = "done"
        if message:
            self._message = message
        self._write(force=True)
        self._log(f"{message} ({time.time() - self.started_at:.1f}s)")

    def fail(self, exc: BaseException) -> None:
        self.state = "error"
        self._message = f"{type(exc).__name__}: {exc}"
        self._write(force=True, error=self._message)
        self._log(f"ERROR: {self._message}", err=True)

    # -- persistence ---------------------------------------------------

    def _write(self, force: bool = False, error: str = "") -> None:
        self._last_flush = time.time()
        self._since_flush = 0
        if not self.write_status:
            return
        entry = self._entry(self.state)
        entry["error"] = error
        entry["updated"] = now_iso()
        try:
            _merge(entry)
        except OSError:
            pass

    def _log(self, message: str, err: bool = False) -> None:
        stream = sys.stderr if err else self.stream
        if not message:
            return
        if self.total:
            print(f"[{self.builder}] {self.done}/{self.total} ({self.pct()}%) {message}",
                  file=stream, flush=True)
        else:
            print(f"[{self.builder}] {message}", file=stream, flush=True)


def run_builder(builder: str, build, *args, **kwargs) -> int:
    """CLI helper: run `build(progress=...)` with a persisted Progress.

    Keeps the standalone builder commands intact while sharing the chunked,
    status-writing behaviour bin/index_jobs.py drives.
    """
    progress = Progress(builder)
    progress.start()
    try:
        result = build(progress, *args, **kwargs)
    except SystemExit:
        raise
    except BaseException as exc:  # noqa: BLE001 - builders report, never trace-crash
        progress.fail(exc)
        return 1
    if result is False:
        return 1
    return 0
