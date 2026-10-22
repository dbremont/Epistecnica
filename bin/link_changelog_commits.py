#!/usr/bin/env python3
"""
Backfill commit links into the corpus changelogs for one change set.

Run AFTER committing the change set whose changelog logs were appended. It
finds the logs the commit introduced and stamps them with:

  commit  the sha of the commit that introduced the change
  before  the sha of its parent (the "state before"); omitted when the file
          did not exist at the parent commit (file created here)

The "state after" is the introducing commit itself, so no separate field.

Changelog entries are authored WITHOUT these fields and committed together
with the corpus file (see AGENTS.md invariant); the links are filled in a
following, json-only annotation commit, which touches no *.md. Going-forward
only: entries created before this tool are left unlinked.

Covers the corpora that keep an authored changelog:

    note      src/note/app/data/changelog.json      (data/ prefix)
    document  src/document/app/data/changelog.json  (documents/ prefix)
    course    src/course/app/data/changelog.json    (courses/ prefix)

    python bin/link_changelog_commits.py                     # HEAD, all corpora
    python bin/link_changelog_commits.py --corpus document
    python bin/link_changelog_commits.py --commit <sha>
    python bin/link_changelog_commits.py --check             # report only, write nothing

Idempotent: logs that already carry a commit are left untouched.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

CORPORA = {
    "note": {
        "data": "src/note/app/data/",
        "changelog": "src/note/app/data/changelog.json",
    },
    "document": {
        "data": "src/document/app/documents/",
        "changelog": "src/document/app/data/changelog.json",
    },
    "course": {
        "data": "src/course/app/courses/",
        "changelog": "src/course/app/data/changelog.json",
    },
}

LOG_KEY_ORDER = ("date", "kind", "summary", "commit", "before")


def git(*args, check=True):
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True,
        text=True,
        check=check,
    )


def changed_files(sha, prefix):
    # Return corpus-relative paths (changelog file_path form), not repo paths.
    out = git("diff-tree", "--no-commit-id", "--name-only", "-r", sha)
    files = set()
    for line in out.stdout.splitlines():
        f = line.strip()
        if f.startswith(prefix):
            files.add(f[len(prefix):])
    return files


def commit_date(sha):
    out = git("show", "-s", "--format=%ad", "--date=short", sha)
    return out.stdout.strip()


def exists_at(sha, prefix, path):
    rel = f"{prefix}{path}"
    return git("cat-file", "-e", f"{sha}:{rel}", check=False).returncode == 0


def ordered_log(log):
    out = {}
    for k in LOG_KEY_ORDER:
        if k in log:
            out[k] = log[k]
    for k, v in log.items():
        if k not in out:
            out[k] = v
    return out


def main(argv=None):
    p = argparse.ArgumentParser(prog="link_changelog_commits.py")
    p.add_argument("--corpus", choices=sorted(CORPORA), action="append",
                   help="Corpus to stamp (repeatable; default: all).")
    p.add_argument("--commit", default="HEAD", help="Change-set commit to link (default: HEAD).")
    p.add_argument("--check", action="store_true", help="Report what would change; write nothing.")
    args = p.parse_args(argv)

    sha = git("rev-parse", args.commit).stdout.strip()
    parent = git("rev-parse", f"{sha}^").stdout.strip()
    cdate = commit_date(sha)

    total = 0
    for name in (args.corpus or sorted(CORPORA)):
        spec = CORPORA[name]
        prefix = spec["data"]
        path = REPO / spec["changelog"]
        if not path.exists():
            print(f"ERROR: {path} not found.", file=sys.stderr)
            return 1

        files = changed_files(sha, prefix)
        data = json.loads(path.read_text(encoding="utf-8"))

        stamped = 0
        warnings = []
        for entry in data:
            rel = entry.get("file_path", "")
            if rel not in files:
                continue
            logs = entry.get("logs")
            if not logs:
                warnings.append(f"{rel}: changed but has no log")
                continue
            last = logs[-1]
            if "commit" in last:
                continue
            if last.get("date") and last["date"] != cdate:
                warnings.append(
                    f"{rel}: last log dated {last['date']} != commit {cdate}; "
                    "stamping anyway"
                )
            last["commit"] = sha
            if exists_at(parent, prefix, rel):
                last["before"] = parent
            logs[-1] = ordered_log(last)
            stamped += 1

        print(f"{name}: {len(files)} changed files, {stamped} log(s) to stamp")
        if args.check:
            for w in warnings:
                print(f"  ! {w}")
            continue

        if stamped:
            # Rewrite in schema key order for every log (stable, canonical layout).
            for entry in data:
                entry["logs"] = [ordered_log(l) for l in entry.get("logs", [])]
            path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        total += stamped
        for w in warnings:
            print(f"  ! {w}")

    if args.check:
        return 0
    if total:
        print(f"stamped {total} log(s) with commit {sha}")
        print("then commit the annotation, e.g.:")
        print("  git commit -m 'chore: link changelog history to commits'")
    else:
        print("nothing to stamp (already linked or no matching logs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
