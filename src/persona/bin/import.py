#!/usr/bin/env python3
"""
Personas importer: Notion export -> corpus.

One-off migration tool. Reads a Notion database export (the "Catálogo
de Personas" folder: per-person markdown files named "<Name>
<32-hex-uuid>.md", plus per-entry asset folders holding images) and
writes the personas corpus: one <slug>.md per person under
src/persona/app/personas/.

- Every file becomes a `type: person` entry: the export holds people,
  so the type is fixed (the catalog facets derive from the data, and
  the vocabulary simply grows). The name is preserved as the markdown
  H1 (fallback: the filename without the uuid suffix).
- The bare Notion `tags:` property line is removed from the body and
  embedded as `tags: [...]` front matter (normalized to the corpus
  naming rules). Slugs follow the corpus naming rules (see
  src/persona/README.md): ASCII, lowercase, kebab-case;
  accent-folded; uuid suffixes removed; collisions get a numeric
  suffix.
- Notion noise is stripped: bare `: <number>` property lines,
  ellipsis-only (`> …`) placeholder blockquotes, and `## Index`
  headings with no content under them. Everything else is kept
  verbatim.
- Referenced images are copied beside their entry into
  personas/<slug>/ (spaces lowercased to hyphens) and their links are
  rewritten to qualified relative paths (`personas/<slug>/<file>` —
  qualified because the viewer renders at /persona/ while entries live
  under personas/). Missing image files print as warnings.
- Everything else is kept verbatim — the corpus becomes the source of
  truth. Existing corpus files (e.g. hand-written seeds) are never
  overwritten: colliding slugs get a numeric suffix.

The export CSVs duplicate the md `tags:` lines and carry only ordering
noise, so they are deliberately not read — the .md files are the
source.

Run the indexer afterwards: python3 src/persona/bin/index.py

Usage: python3 src/persona/bin/import.py <notion-export-dir>
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

PERSONA = Path(__file__).resolve().parent.parent
CORPUS = PERSONA / "app" / "personas"

UUID_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}(?=\.md$)")
TAGS_LINE_RE = re.compile(r"^\s*tags:\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
NOISE_NUMBER_RE = re.compile(r"^\s*:\s*\d+\s*$")
ELLIPSIS_QUOTE_RE = re.compile(r"^\s*>\s*(…|\.\.\.|…\s*…)\s*$")
# Image targets may contain parens and spaces (Notion asset dirs embed
# the entry title), so match greedily up to the closing paren after
# .png on the same line.
IMG_RE = re.compile(r"!\[([^\]]*)\]\((.*\.png)\)")

ENTRY_TYPE = "person"


def fold(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text)
    return folded.encode("ascii", "ignore").decode("ascii")


def kebab(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", fold(text).lower()).strip("-")


def free_path(directory: Path, slug: str, collisions: list) -> Path:
    candidate = directory / f"{slug}.md"
    n = 2
    while candidate.exists():
        candidate = directory / f"{slug}-{n}.md"
        n += 1
    if n > 2:
        collisions.append(candidate.name)
    return candidate


def parse_h1(md: str, fallback: str) -> str:
    for line in md.splitlines():
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
    return fallback


def clean_body(md: str) -> tuple:
    """Strip tags line + Notion noise; return (body, tags)."""
    tags = []
    lines = []
    for line in md.splitlines():
        m = TAGS_LINE_RE.match(line)
        if m:
            for raw in m.group(1).split(","):
                tag = kebab(raw.strip().strip("'\""))
                if tag and tag not in tags:
                    tags.append(tag)
            continue
        if NOISE_NUMBER_RE.match(line):
            continue
        if ELLIPSIS_QUOTE_RE.match(line):
            continue
        lines.append(line)
    lines = drop_empty_index(lines)
    return "\n".join(lines).strip("\n") + "\n", tags


def drop_empty_index(lines: list) -> list:
    """Remove `## Index` headings that have no content under them."""
    out = []
    i = 0
    while i < len(lines):
        m = HEADING_RE.match(lines[i])
        if m and m.group(2).strip().lower() == "index":
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or HEADING_RE.match(lines[j]):
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out


def migrate_images(md: str, export_dir: Path, slug: str,
                   warnings: list) -> tuple:
    """Copy referenced PNGs beside the entry; rewrite their links."""
    asset_dir = CORPUS / slug
    copied = 0

    def fix(m):
        nonlocal copied
        alt, target = m.group(1), m.group(2)
        if not target.lower().endswith(".png"):
            return m.group(0)
        src = export_dir / unquote(target)
        if not src.is_file():
            warnings.append(f"{slug} (missing image '{target}')")
            return m.group(0)
        new_name = re.sub(r"\s+", "-", src.name.strip()).lower()
        asset_dir.mkdir(parents=True, exist_ok=True)
        dest = asset_dir / new_name
        if not dest.exists():
            dest.write_bytes(src.read_bytes())
            copied += 1
        return f"![{alt}](personas/{slug}/{new_name})"

    return IMG_RE.sub(fix, md), copied


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import a Notion 'Catálogo de Personas' export "
                    "into the personas corpus."
    )
    parser.add_argument("export_dir", help="directory holding the export .md files")
    args = parser.parse_args()

    export_dir = Path(args.export_dir)
    if not export_dir.is_dir():
        print(f"ERROR: export directory not found: {export_dir}", file=sys.stderr)
        return 1

    sources = sorted(export_dir.glob("*.md"))
    if not sources:
        print(f"ERROR: no .md files in {export_dir}", file=sys.stderr)
        return 1

    collisions: list = []
    warnings: list = []
    imported = 0
    images = 0

    for path in sources:
        md = path.read_text(encoding="utf-8", errors="replace")
        fallback = UUID_SUFFIX_RE.sub("", path.stem)
        h1 = parse_h1(md, fallback)
        slug = kebab(h1) or kebab(fallback) or "untitled"

        body, tags = clean_body(md)
        body, copied = migrate_images(body, export_dir, slug, warnings)
        images += copied

        out = free_path(CORPUS, slug, collisions)
        tag_list = ", ".join(tags)
        if tag_list:
            text = "---\ntype: %s\ntags: [%s]\n---\n\n%s" % (ENTRY_TYPE, tag_list, body)
        else:
            text = "---\ntype: %s\n---\n\n%s" % (ENTRY_TYPE, body)
        out.write_text(text, encoding="utf-8")
        imported += 1

    print(f"personas-import: {len(sources)} files -> {imported} entries "
          f"(type {ENTRY_TYPE}, {images} images)")
    if collisions:
        print(f"slug collisions (suffixed): {len(collisions)}")
        for c in collisions[:20]:
            print(f"  ! {c}")
    if warnings:
        print(f"warnings: {len(warnings)}")
        for w in warnings[:20]:
            print(f"  ! {w}")
        if len(warnings) > 20:
            print(f"  ! ... and {len(warnings) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
