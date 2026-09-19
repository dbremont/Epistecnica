#!/usr/bin/env python3
"""
Glossarium index builder.

Scans src/glossarium/app/terms/*.md and emits
src/glossarium/app/data/index.json — the lookup corpus for the glossarium
catalog (/glossarium/) and the selection-lookup popup on the note pages.
Stdlib only.

For each term it extracts: slug (filename), name (H1 heading), aliases
(`aliases: [...]` front matter), excerpt (first paragraph, truncated),
lowercased plain text, and word count. Slugs are validated against the
naming convention (see src/glossarium/README.md); violations print as
warnings and never fail the build.

Usage: python3 src/glossarium/bin/index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

GLOSSARIUM = Path(__file__).resolve().parent.parent
APP = GLOSSARIUM / "app"
TERMS = APP / "terms"
OUT = APP / "data" / "index.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ALIASES_RE = re.compile(r"^aliases:\s*\[(.*)\]\s*$")
MARKUP_RE = re.compile(r"[*_>`|]")

EXCERPT_LEN = 240


def plain_text(md: str) -> str:
    lines = []
    for line in md.splitlines():
        line = HEADING_RE.sub(" ", line)
        line = re.sub(r"^>\s?", "", line)
        line = MARKUP_RE.sub(" ", line)
        lines.append(line)
    return re.sub(r"\s+", " ", "\n".join(lines)).strip().lower()


def parse(path: Path):
    md = path.read_text(encoding="utf-8", errors="replace")

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
        name = path.stem.replace("-", " ")

    text = plain_text(md)
    excerpt = text[:EXCERPT_LEN].strip()
    if len(text) > EXCERPT_LEN:
        excerpt = excerpt[:excerpt.rfind(" ")] + " …"
    return name, aliases, excerpt, text


def main() -> int:
    if not TERMS.is_dir():
        print(f"ERROR: terms directory not found: {TERMS}", file=sys.stderr)
        return 1

    warnings = []
    terms = []
    for path in sorted(TERMS.glob("*.md")):
        if not NAME_RE.match(path.stem):
            warnings.append(path.name)
        name, aliases, excerpt, text = parse(path)
        terms.append(
            {
                "slug": path.stem,
                "name": name,
                "aliases": aliases,
                "excerpt": excerpt,
                "text": text,
                "words": len(text.split()),
            }
        )

    terms.sort(key=lambda t: t["name"].lower())

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(terms),
        "terms": terms,
    }
    OUT.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    kb = OUT.stat().st_size / 1024
    total_aliases = sum(len(t["aliases"]) for t in terms)
    print(
        f"glossarium-index: {len(terms)} terms, {total_aliases} aliases,"
        f" {sum(t['words'] for t in terms)} words ->"
        f" {OUT.relative_to(GLOSSARIUM.parent.parent)} ({kb:.0f} KB)"
    )
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/glossarium/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
