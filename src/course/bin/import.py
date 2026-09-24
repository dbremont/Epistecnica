#!/usr/bin/env python3
"""
Courses importer: Notion export -> corpus.

One-off migration tool. Reads a Notion database export (the "Histórico
de Cursos" folder: per-course markdown files named "<Course name>
<32-hex-uuid>.md", plus per-entry asset folders holding images) and
writes the courses corpus: one directory per course under
src/course/app/courses/<slug>/ holding the readme.md entry.

- Every file becomes an entry-only course (readme.md, no lectures):
  the export holds whole-course single pages, so no lecture structure
  is fabricated. The H1 is preserved verbatim (fallback: the filename
  without the uuid suffix).
- The Notion `Tags:` property line is removed from the body and
  embedded as `tags: [...]` front matter (normalized to the corpus
  naming rules). Slugs follow the corpus naming rules (see
  src/course/README.md): ASCII, lowercase, kebab-case;
  accent-folded; uuid suffixes removed; collisions get a numeric
  suffix.
- Notion noise is stripped: bare `: <number>` property lines,
  ellipsis-only (`> …`) placeholder blockquotes, and `## Index`
  headings with no content under them. Everything else is kept
  verbatim.
- Referenced images are copied into the course directory (spaces
  lowercased to hyphens) and their links are rewritten to qualified
  relative paths (`courses/<slug>/<file>` — qualified because the
  course view renders at /course/ while entries live under courses/).
  Missing image files print as warnings.
- Existing course directories (e.g. hand-written seeds) are never
  touched: colliding slugs are skipped with a warning — the corpus
  becomes the source of truth.

Run the indexer afterwards: python3 src/course/bin/index.py

Usage: python3 src/course/bin/import.py <notion-export-dir>
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

COURSE = Path(__file__).resolve().parent.parent
CORPUS = COURSE / "app" / "courses"
ENTRY_FILE = "readme.md"

UUID_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}(?=\.md$)")
TAGS_LINE_RE = re.compile(r"^\s*Tags:\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
NOISE_NUMBER_RE = re.compile(r"^\s*:\s*\d+\s*$")
ELLIPSIS_QUOTE_RE = re.compile(r"^\s*>\s*(…|\.\.\.|…\s*…)\s*$")
# Image targets may contain parens and spaces (Notion asset dirs embed
# the entry title), so match greedily up to the closing paren after
# .png on the same line.
IMG_RE = re.compile(r"!\[([^\]]*)\]\((.*\.png)\)")


def fold(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text)
    return folded.encode("ascii", "ignore").decode("ascii")


def kebab(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", fold(text).lower()).strip("-")


def slugify(name: str) -> str:
    return kebab(name)


def free_slug(base: str, taken: set, collisions: list) -> str:
    slug = base or "untitled"
    n = 2
    while slug in taken:
        slug = f"{base}-{n}"
        n += 1
    if slug != base:
        collisions.append(slug)
    taken.add(slug)
    return slug


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
    """Copy referenced PNGs into the course dir; rewrite their links."""
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
        return f"![{alt}](courses/{slug}/{new_name})"

    return IMG_RE.sub(fix, md), copied


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import a Notion 'Histórico de Cursos' export "
                    "into the courses corpus."
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

    taken: set = set()
    collisions: list = []
    warnings: list = []
    skipped: list = []
    imported = 0
    images = 0

    for path in sources:
        md = path.read_text(encoding="utf-8", errors="replace")
        fallback = UUID_SUFFIX_RE.sub("", path.stem)
        h1 = parse_h1(md, fallback)
        base = slugify(h1) or slugify(fallback) or "untitled"
        slug = free_slug(base, taken, collisions)
        course_dir = CORPUS / slug
        if (course_dir / ENTRY_FILE).exists():
            skipped.append(slug)
            continue

        body, tags = clean_body(md)
        body, copied = migrate_images(body, export_dir, slug, warnings)
        images += copied

        course_dir.mkdir(parents=True, exist_ok=True)
        if tags:
            text = "---\ntags: [%s]\n---\n\n%s" % (", ".join(tags), body)
        else:
            text = body
        (course_dir / ENTRY_FILE).write_text(text, encoding="utf-8")
        imported += 1

    print(f"courses-import: {len(sources)} files -> {imported} courses "
          f"({len(skipped)} skipped, {images} images)")
    if collisions:
        print(f"slug collisions (suffixed): {len(collisions)}")
        for c in collisions[:20]:
            print(f"  ! {c}")
    if skipped:
        print(f"skipped (readme exists): {len(skipped)}")
        for s in skipped:
            print(f"  - {s}")
    if warnings:
        print(f"warnings: {len(warnings)}")
        for w in warnings[:20]:
            print(f"  ! {w}")
        if len(warnings) > 20:
            print(f"  ! ... and {len(warnings) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
