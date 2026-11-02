#!/usr/bin/env python3
"""
Add one glossarium term to the Epistecnica lexical corpus.

Reads a markdown file, parses it with the glossarium conventions — the term
name from the first `# ` heading, optional `aliases: [...]` front matter, the
rest as the body — and upserts `{slug, name, aliases, body}` into
src/glossarium/app/data/terms.json (the source of truth, keyed by slug). The file
is re-sorted by name. Stdlib only.

The slug (term code) defaults to the markdown filename stem and must be
kebab-case; pass --slug to set it explicitly. After adding, run
`make glossarium-index` to regenerate the derived index.

Usage:
    python3 bin/add_glossarium_term.py path/to/term.md [--slug <code>]
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

from indexlib import atomic_write_text

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "src" / "glossarium" / "app" / "data" / "terms.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ALIASES_RE = re.compile(r"^aliases:\s*\[(.*)\]\s*$")


def parse(md: str, slug: str):
    """Return (name, aliases, body) per the glossarium conventions."""
    aliases = []
    fm = FRONT_MATTER_RE.match(md)
    if fm:
        for line in fm.group(1).splitlines():
            m = ALIASES_RE.match(line.strip())
            if m:
                aliases = [
                    a.strip().strip("'\"")
                    for a in m.group(1).split(",")
                    if a.strip()
                ]
        md = md[fm.end():]

    name = None
    for line in md.splitlines():
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            name = m.group(2).strip()
            break
    if name is None:
        name = slug.replace("-", " ")
    return name, aliases, md


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="add_glossarium_term.py",
        description="Add/replace one term in src/glossarium/app/data/terms.json.",
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
    name, aliases, body = parse(md, slug)
    entry = {"slug": slug, "name": name, "aliases": aliases, "body": body}

    if SRC.is_file():
        try:
            data = json.loads(SRC.read_text(encoding="utf-8"))
        except ValueError as exc:
            print(f"ERROR: invalid JSON in {SRC}: {exc}", file=sys.stderr)
            return 1
    else:
        data = {}
    if not isinstance(data, dict):
        data = {}
    terms = data.get("terms") if isinstance(data.get("terms"), list) else []

    replaced = any(isinstance(t, dict) and t.get("slug") == slug for t in terms)
    terms = [t for t in terms if not (isinstance(t, dict) and t.get("slug") == slug)]
    terms.append(entry)
    terms.sort(key=lambda t: (t.get("name") or "").lower())

    payload = {
        "generated": date.today().isoformat(),
        "count": len(terms),
        "terms": terms,
    }
    atomic_write_text(SRC, json.dumps(payload, ensure_ascii=False, separators=(",", ":")))

    action = "replaced" if replaced else "added"
    print(
        f"glossarium-add: {action} '{name}' ({slug}) ->"
        f" {SRC.relative_to(REPO)} ({len(terms)} terms)"
    )
    print("run: make glossarium-index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
