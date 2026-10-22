#!/usr/bin/env python3
"""
Backfill a corpus changelog from git history.

Builds the per-file changelog for a corpus that does not have one yet
(src/document/app/data/changelog.json, src/course/app/data/changelog.json)
by walking the commits that touched the corpus documents and recording one
log per changed markdown file. Unlike the note corpus changelog (authored
by hand per change set), these logs are generated: every entry already
carries the `commit` sha and the parent `before` sha, and the `summary` is
the commit subject.

    python3 bin/backfill_changelog.py --corpus document
    python3 bin/backfill_changelog.py --corpus course
    python3 bin/backfill_changelog.py --corpus document --check

Idempotent: re-running regenerates the same file from history. Deletions
(files that no longer exist) and merge commits are skipped. The note corpus
is not backfilled here: its changelog is authored per change set and linked
post-commit by bin/link_changelog_commits.py.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

CORPORA = {
    "document": {
        "docs": "src/document/app/documents/",
        "out": "src/document/app/data/changelog.json",
    },
    "course": {
        "docs": "src/course/app/courses/",
        "out": "src/course/app/data/changelog.json",
    },
}

KINDS = {"feat", "fix", "docs", "style", "refactor", "test", "chore"}
SUBJECT_RE = re.compile(r"^([a-z]+)(?:\([^)]*\))?!?:\s*")


def git(*args, check=True):
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True,
        text=True,
        check=check,
    )


def commits(prefix):
    out = git("log", "--reverse", "--no-merges", f"--format=%H%x1f%ad%x1f%s",
              "--date=short", "--", prefix)
    for line in out.stdout.splitlines():
        if not line.strip():
            continue
        sha, cdate, subject = line.split("\x1f", 2)
        yield sha, cdate, subject


def changed(sha, prefix):
    out = git("diff-tree", "--no-commit-id", "--name-status", "-r", "-M", sha,
              "--", prefix)
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0][:1]
        path = parts[-1].strip()
        if status == "D" or not path.endswith(".md"):
            continue
        yield path


def exists_at(sha, repo_path):
    return git("cat-file", "-e", f"{sha}:{repo_path}", check=False).returncode == 0


def parse_subject(subject):
    m = SUBJECT_RE.match(subject)
    if not m:
        return None, subject
    kind = m.group(1) if m.group(1) in KINDS else None
    return kind, subject[m.end():].strip() or subject


def backfill(corpus):
    spec = CORPORA[corpus]
    prefix = spec["docs"]
    out = REPO / spec["out"]

    entries = {}
    for sha, cdate, subject in commits(prefix):
        parent = git("rev-parse", f"{sha}^").stdout.strip()
        for repo_path in sorted(changed(sha, prefix)):
            rel = repo_path[len(prefix):]
            log = {"date": cdate}
            kind, summary = parse_subject(subject)
            if kind:
                log["kind"] = kind
            log["summary"] = summary
            log["commit"] = sha
            if exists_at(parent, repo_path):
                log["before"] = parent
            entries.setdefault(rel, []).append(log)

    docs_dir = REPO / prefix
    data = [{"file_path": path, "logs": logs}
            for path, logs in sorted(entries.items())
            if (docs_dir / path).is_file()]
    return data, out


def main(argv=None):
    p = argparse.ArgumentParser(prog="backfill_changelog.py")
    p.add_argument("--corpus", required=True, choices=sorted(CORPORA))
    p.add_argument("--check", action="store_true", help="Report what would change; write nothing.")
    args = p.parse_args(argv)

    data, out = backfill(args.corpus)
    logs = sum(len(e["logs"]) for e in data)
    print(f"{args.corpus}: {len(data)} files, {logs} logs -> {out.relative_to(REPO)}")

    if args.check:
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print("written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
