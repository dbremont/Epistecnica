#!/usr/bin/env python3
"""
Notes importer: Notion export block -> corpus section.

Reads a Notion page export (the folder holding "<Page name> <32-hex-uuid>.md"
files and their subpage folders) and writes it as a section of the notes
corpus, targeting any subtree named by --into (e.g. technica/security).

Normalization is mechanical; no content is rewritten beyond what the corpus
naming rules require:

- The export's top folder is the scope root. The root page (the markdown file
  beside it) becomes the section's entry note, named after the target dir.
- File names come from the H1 (fallback: the file name without the uuid),
  slugified to ASCII lowercase kebab-case; uuid suffixes are removed.
- Directories whose name carries "conceptual-model" are dissolved, following
  the corpus rule that the parent already names the subject: the wrapper is a
  level, not a statement.
- Front matter is built as `tags: [note, <--tag…>, <direction>, <notion tag>]`.
  The Notion "Tags" property line and the bare ": <number>" relation-count
  lines are removed from the body.
- Notion back-relation property lines (": A (A%20uuid.md), B (…)" ) become a
  one-line "> Related: …" with real links.
- Notion "topic" placeholder pages and database CSV exports are skipped.
- Links to other pages in the same export are rewritten to absolute viewer
  URLs; images are copied into the shared asset store and referenced
  page-root-relative.

Run the indexer afterwards: python3 bin/notes_index.py

Usage: python3 bin/notes_import.py <export-dir> --into technica/security
"""

import argparse
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "src" / "corpus" / "notes"
ASSETS = REPO / "src" / "app" / "assets" / "note"

UUID_SUFFIX = re.compile(r"\s+[0-9a-f]{32}$")
PROPERTY_COUNT = re.compile(r"^\s*:\s*\d+\s*$")
NOTION_TAGS = re.compile(r"^tags:\s*(.+?)\s*$")
RELATION = re.compile(r"^\s*:\s*(\S.*)$")
RELATION_LINK = re.compile(r"\(([^()]*(?:\([^()]*\)[^()]*)*\.md)\)")
MD_LINK = re.compile(r"\]\((.+?\.md)((?:#[^)\s]*)?)\)")
IMG_LINK = re.compile(r"!\[([^\]]*)\]\((.+?\.(?:png|jpe?g|gif|svg|webp))\)")
ELLIPSIS_QUOTE = re.compile(r"^>\s*…\s*$")
CSV_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\.csv\)")
NOTION_PAGE = re.compile(r"\[([^\]]*)\]\(https?://app\.notion\.com/[^)]*\)")
EMPTY_QUOTE_LINE = re.compile(r"^>\s*(See more in)?\s*\.?\s*$")
INDEX_HEADING = re.compile(r"^##+\s+Index\s*$")

# Spelling corrections applied to slugs and titles on the way in. Both are
# slips in the source export, not a preference of ours.
SLUG_FIXES = {"permision-model": "permission-model", "thread-model": "threat-model", "x-509": "x509"}
TITLE_FIXES = {"Thread Model": "Threat Model", "Permision Model": "Permission Model"}
TAG_FIXES = {"thread": "threat", "permision": "permission"}
SKIP_STEMS = {"topic"}
EXTRA_TAGS = []
TITLES = {}


def slug(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return SLUG_FIXES.get(text, text) or "untitled"


def title_of(p):
    for line in p.read_text(errors="ignore").splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            return TITLE_FIXES.get(t, t)
    return SLUG_FIXES.get(slug(UUID_SUFFIX.sub("", p.stem)), UUID_SUFFIX.sub("", p.stem))


def is_wrapper(part):
    low = part.lower().replace("-", " ")
    return "conceptual model" in low


def clean_dir_parts(parts):
    out = []
    for part in parts:
        if is_wrapper(part):
            continue
        s = slug(UUID_SUFFIX.sub("", part))
        if s:
            out.append(s)
    return out


def plan(export, into):
    """Return (moves, path_map): planned notes and export-path -> corpus-path."""
    export = export.resolve()
    mds = sorted(export.rglob("*.md"))
    tops = {p.name for p in export.iterdir() if p.is_dir()}
    if len(tops) != 1:
        sys.exit(f"expected one top-level folder in the export, found: {sorted(tops)}")
    scope = (export / tops.pop())

    into_parts = [p for p in into.strip("/").split("/") if p]
    master_slug = into_parts[-1]

    moves, path_map = [], {}
    for p in mds:
        if p.stem.lower().startswith(tuple(SKIP_STEMS)):
            continue
        rel = p.relative_to(export)
        if rel.parent == Path("."):
            corpus_rel = Path(*into_parts, f"{master_slug}.md")
        else:
            inside = p.relative_to(scope)
            parts = clean_dir_parts(inside.parent.parts)
            corpus_rel = Path(*into_parts, *parts, f"{slug(title_of(p))}.md")
        key = rel.as_posix()
        path_map[key] = corpus_rel.as_posix()
        moves.append((p, rel, corpus_rel, title_of(p)))
    return export, into_parts, master_slug, moves, path_map


def render(p, rel, corpus_rel, title, path_map, into_parts, dry_run):
    text = p.read_text(errors="ignore")
    lines = text.splitlines()

    # ---- front matter
    tags = ["note"]
    for t in EXTRA_TAGS:
        if t not in tags:
            tags.append(t)
    parts = [x for x in rel.parent.parts if x and not is_wrapper(x)][1:]
    direction = slug(parts[0]) if parts else ""
    notion_tag = ""
    body = []
    for line in lines:
        m = NOTION_TAGS.match(line) if notion_tag == "" else None
        if m:
            notion_tag = slug(m.group(1))
            continue
        if PROPERTY_COUNT.match(line) or ELLIPSIS_QUOTE.match(line):
            continue
        body.append(line)

    if not direction:
        direction = corpus_rel.stem
    if direction != into_parts[-1] and direction not in tags:
        tags.append(direction)
    if notion_tag and notion_tag not in tags:
        tags.append(TAG_FIXES.get(notion_tag, notion_tag))

    # ---- body: relations, links, images
    note_dir = corpus_rel.parent
    out = []
    for line in body:
        m = RELATION.match(line)
        if m and ".md" in m.group(1) and not line.strip().startswith("::"):
            items = []
            for target in RELATION_LINK.findall(m.group(1)):
                resolved = resolve_link(target, rel, path_map)
                fallback = UUID_SUFFIX.sub("", unquote(target).rsplit("/", 1)[-1][:-3])
                label = TITLES.get(resolved, fallback) if resolved else fallback
                items.append(f"[{label}](/view.html?p=notes/{resolved})" if resolved else label)
            if items:
                out.append("> Related: " + ", ".join(items))
                continue

        if EMPTY_QUOTE_LINE.match(line):
            continue
        line = CSV_LINK.sub(lambda mm: mm.group(1), line)
        line = NOTION_PAGE.sub(lambda mm: notion_page_label(mm.group(1)), line)

        def md_sub(mm):
            resolved = resolve_link(mm.group(1), rel, path_map)
            return f"](/view.html?p=notes/{resolved}{mm.group(2) or ''})" if resolved else mm.group(0)

        line = MD_LINK.sub(md_sub, line)
        out.append(line)

    for i, line in enumerate(out):
        if line.startswith("# "):
            fixed = TITLE_FIXES.get(line[2:].strip())
            if fixed:
                out[i] = "# " + fixed
            break

    text = "\n".join(out) + "\n"
    text = strip_empty_index(text)

    # ---- images
    def img_sub(mm):
        alt, target = mm.group(1), mm.group(2)
        if target.startswith(("http://", "https://")):
            return mm.group(0)
        src = (p.parent / unquote(target)).resolve()
        if not src.exists():
            print(f"  ! missing image {target} in {rel}")
            return mm.group(0)
        dest = ASSETS / note_dir / corpus_rel.stem / src.name
        new_rel = f"../assets/note/{note_dir.as_posix()}/{corpus_rel.stem}/{src.name}"
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
        return f"![{alt}]({new_rel})"

    text = IMG_LINK.sub(img_sub, text)

    head = "---\ntags: [" + ", ".join(tags) + "]\n---\n\n"
    return head + text


def strip_empty_index(text):
    lines = text.splitlines()
    keep, i = [], 0
    while i < len(lines):
        if INDEX_HEADING.match(lines[i]):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or lines[j].startswith("#"):
                i = j
                continue
        keep.append(lines[i])
        i += 1
    return "\n".join(keep) + "\n"


def notion_page_label(label):
    """A dead Notion page link: relink by title when the page was imported, else keep the text."""
    wanted = label.strip().lower()
    for corpus_path, title in TITLES.items():
        if title.strip().lower() == wanted:
            return f"[{label}](/view.html?p=notes/{corpus_path})"
    return label


def resolve_link(target, rel, path_map):
    decoded = unquote(target)
    resolved = Path(os.path.normpath(os.path.join(str(rel.parent), decoded))).as_posix()
    return path_map.get(resolved)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("export", type=Path)
    ap.add_argument("--into", required=True, help="corpus-relative target, e.g. technica/security")
    ap.add_argument("--tag", action="append", default=[], help="extra front-matter tag (repeatable)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    global EXTRA_TAGS, TITLES
    EXTRA_TAGS = args.tag

    export, into_parts, master_slug, moves, path_map = plan(args.export, args.into)
    TITLES = {dest.as_posix(): title for _src, _rel, dest, title in moves}
    print(f"{len(moves)} notes -> src/corpus/notes/{args.into}/")
    if args.dry_run:
        for src, rel, dest, title in moves:
            print(f"  {rel.as_posix():86s} -> {dest.as_posix()}")
        print(f"  {len(path_map)} link targets mapped")
        return

    written = 0
    for src, rel, dest, title in moves:
        out = NOTES / dest
        if out.exists() and not args.force:
            print(f"  = skip (exists) {dest.as_posix()}")
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(src, rel, dest, title, path_map, into_parts, False))
        written += 1
    print(f"wrote {written} notes; run bin/notes_index.py next")


if __name__ == "__main__":
    import os

    main()
