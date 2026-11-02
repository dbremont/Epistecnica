#!/usr/bin/env python3
"""
Glossarium index builder.

Reads the hand-maintained term corpus src/glossarium/app/data/terms.json
(`{generated, count, terms: [{slug, name, aliases, body}]}`) and emits
src/glossarium/app/data/index.json — the lookup corpus for the glossarium
catalog (/glossarium/), the term search and the select-a-word popup on the
note pages. Stdlib only.

terms.json is the source of truth and is left untouched; index.json is the
only derived artifact (slug, name, aliases, excerpt, lowercased plain text,
word count). Slugs are validated against the naming convention (see
src/glossarium/README.md); violations print as warnings and never fail the
build.

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
SRC = APP / "data" / "terms.json"
OUT = APP / "data" / "index.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
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


def build(progress=None) -> bool:
    if not SRC.is_file():
        print(f"ERROR: terms file not found: {SRC}", file=sys.stderr)
        return False

    try:
        src = json.loads(SRC.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"ERROR: invalid JSON in {SRC}: {exc}", file=sys.stderr)
        return False

    raw_terms = src.get("terms", []) if isinstance(src, dict) else []
    if progress is not None:
        progress.set_total(len(raw_terms))
        progress.start(f"indexing {len(raw_terms)} terms")

    warnings = []
    terms = []
    for t in raw_terms:
        if not isinstance(t, dict):
            continue
        slug = t.get("slug", "")
        name = t.get("name", "") or slug.replace("-", " ")
        aliases = [a for a in (t.get("aliases") or []) if isinstance(a, str)]
        body = t.get("body", "") or ""
        if not NAME_RE.match(slug):
            warnings.append(slug or "(missing slug)")
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
