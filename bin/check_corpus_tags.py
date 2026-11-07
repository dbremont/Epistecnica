#!/usr/bin/env python3
"""Validate the corpus tag convention.

Every markdown file under the three corpora must carry its top-level corpus
tag as the first front-matter tag:

  src/notes/app/data/**/*.md       -> note
  src/documents/app/documents/**   -> document
  src/courses/app/courses/**/*.md  -> course

Metadata-only: this checker never writes.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CORPORA = [
    ("note", REPO / "src" / "notes" / "app" / "data"),
    ("document", REPO / "src" / "documents" / "app" / "documents"),
    ("course", REPO / "src" / "courses" / "app" / "courses"),
]
TAG_RE = re.compile(r"^tags:\s*\[([^\]]*)\]\s*$", re.M)


def main() -> int:
    problems = []
    checked = 0
    for tag, root in CORPORA:
        if not root.is_dir():
            problems.append((root, "missing corpus directory"))
            continue
        for f in sorted(root.rglob("*.md")):
            checked += 1
            text = f.read_text(encoding="utf-8", errors="replace")
            if not text.startswith("---\n"):
                problems.append((f, "no front matter"))
                continue
            end = text.find("\n---", 4)
            if end == -1:
                problems.append((f, "unterminated front matter"))
                continue
            m = TAG_RE.search(text[4:end])
            if not m:
                problems.append((f, "no tags line"))
                continue
            tags = [t.strip() for t in m.group(1).split(",") if t.strip()]
            if not tags or tags[0] != tag:
                problems.append((f, f"first tag is {tags[0]!r}, expected {tag!r}"))
            elif len(tags) != len(set(tags)):
                problems.append((f, "duplicate tag"))
    print(f"[corpus-tags] {checked} files checked")
    if problems:
        for f, why in problems[:20]:
            print(f"  ! {f.relative_to(REPO)}: {why}")
        print(f"[corpus-tags] FAIL: {len(problems)} problem(s)")
        return 1
    print("[corpus-tags] ok: every corpus markdown file carries its top-dir tag first")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
