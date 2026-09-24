#!/usr/bin/env python3
"""
Documents importer: Notion export -> corpus.

One-off migration tool. Reads a Notion database export (the "Catalogus
Documentorum" folder: per-document markdown files named "<Citation>
<32-hex-uuid>.md", plus per-entry asset folders holding images) and
writes the documents corpus: one <slug>.md per document under
src/document/app/documents/{papers,articles,books}/.

- The citation is preserved as the markdown H1 (fallback: the filename
  without the uuid suffix).
- Classification: the bibtex entry type decides the section (@book and
  @inbook -> books; @article -> articles; everything else ->
  papers). Files with a `{bitex reference}` placeholder instead of
  bibtex fall back to venue heuristics on the citation (conference
  pattern -> papers; journal/volume pattern -> articles; publisher
  pattern -> books) and default to articles; defaulted files are
  printed as a review list.
- The Notion `Tags:` property line is removed from the body and
  embedded as `tags: [...]` front matter (normalized to the corpus
  naming rules; the `Unread` status marker is dropped). Slugs follow
  the corpus naming rules (see src/document/README.md): ASCII,
  lowercase, kebab-case; accent-folded; uuid suffixes removed;
  collisions get a numeric suffix.
- Referenced images are copied beside their document into
  documents/<section>/<slug>/ with rewritten section-qualified links
  (`documents/<section>/<slug>/<file>` — qualified because the viewer
  renders at /document/ while entries live under documents/), and never
  overwrites existing files (colliding slugs get a numeric suffix).
- Everything else is kept verbatim — the corpus becomes the source of
  truth. Existing corpus files (e.g. hand-written seeds) are never
  overwritten: colliding slugs get a numeric suffix.

Run the indexer afterwards: python3 src/document/bin/index.py

Usage: python3 src/document/bin/import.py <notion-export-dir>
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

DOCUMENT = Path(__file__).resolve().parent.parent
CORPUS = DOCUMENT / "app" / "documents"

UUID_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}(?=\.md$)")
BIBTEX_RE = re.compile(r"^@([a-zA-Z]+)\s*[{]")
TAGS_LINE_RE = re.compile(r"^\s*Tags:\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
# Image targets may contain parens (Notion asset dirs embed the entry
# title, e.g. "... (2008) Introducti/image.png"), so match greedily up
# to the closing paren after .png on the same line.
IMG_RE = re.compile(r"!\[([^\]]*)\]\((.*\.png)\)")
YEAR_RE = re.compile(r"\b(1[5-9]\d\d|20[0-2]\d)\b")

BOOK_TYPES = {"book", "inbook"}
ARTICLE_TYPES = {"article"}

CONF_RE = re.compile(
    r"proceedings|conference|symposium|workshop|sigcomm|sigmod|sosp|osdi|nsdi",
    re.IGNORECASE,
)
JOURNAL_RE = re.compile(
    r"transactions|journal|magazine|quarterly|review|\bvol\.|chapter|"
    r"\b\d{1,3}\(\d{1,3}\)",
    re.IGNORECASE,
)
BOOK_RE = re.compile(
    r"press|books|verlag|wiley|springer|oxford|cambridge|thesis|dissertation",
    re.IGNORECASE,
)

STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "and", "or", "for", "to", "with",
    "from", "into", "its", "their", "his", "her", "our", "your", "this",
    "that", "these", "those", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "having", "will", "would", "shall",
    "should", "could", "may", "might", "must", "can", "not", "no", "nor",
    "but", "yet", "so", "than", "too", "very", "just", "also", "how",
    "what", "when", "where", "which", "who", "whom", "whose", "why",
    "over", "under", "between", "through", "during", "before", "after",
    "toward", "towards", "upon", "within", "without", "using", "used",
    "use", "based", "new", "toward",
}

DROP_TAGS = {"unread"}


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


def significant(text: str, skip: str, year, limit: int) -> list:
    words = []
    for tok in re.findall(r"[A-Za-zÀ-ÿ']+", text):
        w = kebab(tok.strip("'"))
        if len(w) >= 3 and w not in STOPWORDS and w != year and w != skip:
            words.append(w)
        if len(words) >= limit:
            break
    return words


def make_slug(h1: str) -> str:
    year = None
    ym = YEAR_RE.search(h1)
    head, tail = h1, ""
    if ym:
        year = ym.group(1)
        head, tail = h1[: ym.start()], h1[ym.end():]
    author = ""
    for tok in re.findall(r"[A-Za-zÀ-ÿ']+", head):
        clean = tok.strip("'")
        if len(clean) > 1:
            author = kebab(clean)
            break
    words = significant(tail, author, year, 5)
    if len(words) < 3:
        words = significant(head + " " + tail, author, year, 5)
    parts = [p for p in [author, year] + words if p]
    slug = "-".join(parts)[:64].strip("-")
    return slug or "untitled"


def classify(md: str, h1: str, stats: dict) -> tuple:
    """Return (section, method) for one document body."""
    head = "\n".join(md.splitlines()[:40])
    for line in head.splitlines():
        m = BIBTEX_RE.match(line.strip())
        if m:
            kind = m.group(1).lower()
            stats["bibtex:" + kind] = stats.get("bibtex:" + kind, 0) + 1
            if kind in BOOK_TYPES:
                return "books", "bibtex"
            if kind in ARTICLE_TYPES:
                return "articles", "bibtex"
            return "papers", "bibtex"
    probe = h1 + "\n" + head
    if CONF_RE.search(probe):
        return "papers", "heuristic-conf"
    if JOURNAL_RE.search(probe):
        return "articles", "heuristic-journal"
    if BOOK_RE.search(probe):
        return "books", "heuristic-book"
    return "articles", "default"


def split_tags(md: str) -> tuple:
    """Return (body_without_tags_line, normalized_tags)."""
    tags = []
    kept = []
    for line in md.splitlines():
        m = TAGS_LINE_RE.match(line)
        if m:
            for raw in m.group(1).split(","):
                tag = kebab(raw.strip().strip("'\""))
                if not tag or tag in DROP_TAGS:
                    continue
                if tag not in tags:
                    tags.append(tag)
        else:
            kept.append(line)
    return "\n".join(kept).strip("\n") + "\n", tags


def migrate_images(md: str, export_dir: Path, section: str, slug: str,
                   warnings: list) -> tuple:
    """Copy referenced PNGs beside the document; rewrite their links."""
    asset_dir = CORPUS / section / slug
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
        return f"![{alt}](documents/{section}/{slug}/{new_name})"

    return IMG_RE.sub(fix, md), copied


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import a Notion 'Catalogus Documentorum' export "
                    "into the documents corpus."
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

    stats: dict = {}
    collisions: list = []
    warnings: list = []
    review: list = []
    images = 0

    for path in sources:
        md = path.read_text(encoding="utf-8", errors="replace")
        fallback = UUID_SUFFIX_RE.sub("", path.stem)
        h1 = parse_h1(md, fallback)
        section, method = classify(md, h1, stats)
        stats[method] = stats.get(method, 0) + 1
        if method == "default":
            review.append(f"{section}/{h1[:80]}")
        slug = make_slug(h1) or kebab(fallback) or "untitled"

        body, tags = split_tags(md)
        body, copied = migrate_images(body, export_dir, section, slug, warnings)
        images += copied

        out = free_path(CORPUS / section, slug, collisions)
        out.parent.mkdir(parents=True, exist_ok=True)
        if tags:
            text = "---\ntags: [%s]\n---\n\n%s" % (", ".join(tags), body)
        else:
            text = body
        out.write_text(text, encoding="utf-8")
        stats[section] = stats.get(section, 0) + 1

    print(f"documents-import: {len(sources)} files -> "
          f"{stats.get('papers', 0)} papers, {stats.get('articles', 0)} articles, "
          f"{stats.get('books', 0)} books ({images} images)")
    for key in sorted(stats):
        if key in ("papers", "articles", "books"):
            continue
        print(f"  {key}: {stats[key]}")
    if collisions:
        print(f"slug collisions (suffixed): {len(collisions)}")
        for c in collisions[:20]:
            print(f"  ! {c}")
    if review:
        print(f"default-section review list ({len(review)} -> articles):")
        for r in review[:40]:
            print(f"  ? {r}")
        if len(review) > 40:
            print(f"  ? ... and {len(review) - 40} more")
    if warnings:
        print(f"warnings: {len(warnings)}")
        for w in warnings[:20]:
            print(f"  ! {w}")
        if len(warnings) > 20:
            print(f"  ! ... and {len(warnings) - 20} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
