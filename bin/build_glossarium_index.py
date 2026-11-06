#!/usr/bin/env python3
"""
Glossarium index builder.

Scans the hand-maintained term corpus src/glossarium/app/terms/*.md — one
markdown file per term — and emits src/glossarium/app/data/index.json, the
lookup corpus for the glossarium catalog (/glossarium/), the term search and
the select-a-word popup on the note pages. Stdlib only.

Each file is the term: the slug is the filename stem, the name is the first
`# ` heading, `aliases: [...]` front matter carries the alternative spellings,
and the rest is the body. The markdown is the source of truth and is served
as-is at /glossarium/terms/<slug>.md; index.json is the only derived artifact
(slug, name, aliases, excerpt, lowercased plain text, word count). Slugs are
validated against the naming convention (see src/glossarium/README.md);
violations print as warnings and never fail the build.

The build is chunked and progress-aware (bin/indexlib.py), so
bin/index_jobs.py can run it in the background like every other builder.

Usage: python3 bin/build_glossarium_index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

from indexlib import atomic_write_text, run_builder

REPO = Path(__file__).resolve().parent.parent
APP = REPO / "src" / "glossarium" / "app"
SRC = APP / "terms"
OUT = APP / "data" / "index.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ALIASES_RE = re.compile(r"^aliases:\s*\[(.*)\]\s*$")
MARKUP_RE = re.compile(r"[*_>`|]")

EXCERPT_LEN = 240


def plain_text(md: str) -> str:
    """Lowercased, markup-stripped single-line text (catalog search corpus)."""
    lines = []
    for line in md.splitlines():
        line = HEADING_RE.sub(" ", line)
        line = re.sub(r"^>\s?", "", line)
        line = MARKUP_RE.sub(" ", line)
        lines.append(line)
    return re.sub(r"\s+", " ", "\n".join(lines)).strip().lower()


def excerpt(text: str) -> str:
    cut = text[:EXCERPT_LEN].strip()
    if len(text) > EXCERPT_LEN:
        cut = cut[:cut.rfind(" ")] + " …"
    return cut


def parse(path: Path):
    """Return (name, aliases, body) per the glossarium conventions."""
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
    return name, aliases, md


def build(progress=None) -> bool:
    if not SRC.is_dir():
        print(f"ERROR: terms directory not found: {SRC}", file=sys.stderr)
        return False

    files = sorted(SRC.glob("*.md"))
    if progress is not None:
        progress.set_total(len(files))
        progress.start(f"indexing {len(files)} terms")

    warnings = []
    terms = []
    for path in files:
        slug = path.stem
        name, aliases, body = parse(path)
        if not NAME_RE.match(slug):
            warnings.append(f"{slug} (not kebab-case)")
        if not body.lstrip().startswith("# "):
            warnings.append(f"{slug} (no `# ` heading; name falls back to the slug)")
        text = plain_text(body)
        terms.append({
            "slug": slug,
            "name": name,
            "aliases": aliases,
            "excerpt": excerpt(text),
            "text": text,
            "words": len(text.split()),
        })
        if progress is not None:
            progress.step(message=slug)

    terms.sort(key=lambda t: t["name"].lower())

    if progress is not None:
        progress.stage(f"writing {OUT.name}")

    payload = {
        "generated": date.today().isoformat(),
        "count": len(terms),
        "terms": terms,
    }
    atomic_write_text(OUT, json.dumps(payload, ensure_ascii=False, separators=(",", ":")))

    kb = OUT.stat().st_size / 1024
    total_aliases = sum(len(t["aliases"]) for t in terms)
    print(
        f"glossarium-index: {len(terms)} terms, {total_aliases} aliases,"
        f" {sum(t['words'] for t in terms)} words ->"
        f" {OUT.relative_to(REPO)} ({kb:.0f} KB)"
    )
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/glossarium/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    if progress is not None:
        progress.finish(f"{len(terms)} terms")
    return True


def main() -> int:
    return run_builder("glossarium", build)


if __name__ == "__main__":
    raise SystemExit(main())
