#!/usr/bin/env python3
"""
Add or replace one glossarium term in the Epistecnica lexical corpus.

The corpus is one markdown file per term: src/glossarium/app/terms/<slug>.md.
The file is the term — the slug is the filename stem, the name is the first
`# ` heading, `aliases: [...]` front matter carries the alternative spellings,
and the rest is the body, served as-is at /glossarium/terms/<slug>.md.

This helper copies a markdown file into the corpus under its slug (default:
the source filename stem), validating the kebab-case slug and the `# ` heading
first, so a malformed term never lands in the corpus. Stdlib only.

After adding, run `make glossarium-index` to regenerate the derived index.

Usage:
    python3 bin/add_glossarium_term.py path/to/term.md [--slug <code>]
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TERMS = REPO / "src" / "glossarium" / "app" / "terms"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
H1_RE = re.compile(r"^#\s+(.*?)\s*#*\s*$", re.MULTILINE)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="add_glossarium_term.py",
        description="Add/replace one term in src/glossarium/app/terms/.",
    )
    parser.add_argument("file", help="Markdown file for the term.")
    parser.add_argument(
        "--slug",
        default=None,
        help="Term code (kebab-case). Defaults to the markdown filename stem.",
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 1

    slug = args.slug or path.stem
    if not NAME_RE.match(slug):
        print(
            f"ERROR: slug '{slug}' is not kebab-case "
            f"(use --slug to set a valid term code).",
            file=sys.stderr,
        )
        return 1

    md = path.read_text(encoding="utf-8", errors="replace")
    heading = H1_RE.search(md)
    if not heading:
        print(
            f"ERROR: {path} has no `# ` heading — the first one is the term name.",
            file=sys.stderr,
        )
        return 1

    TERMS.mkdir(parents=True, exist_ok=True)
    dest = TERMS / f"{slug}.md"
    replaced = dest.exists()
    if not (dest.exists() and dest.resolve() == path.resolve()):
        shutil.copyfile(path, dest)

    print(
        f"glossarium-add: {'replaced' if replaced else 'added'} "
        f"'{heading.group(1)}' ({slug}) -> {dest.relative_to(REPO)}"
        f" ({len(list(TERMS.glob('*.md')))} terms)"
    )
    print("run: make glossarium-index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
