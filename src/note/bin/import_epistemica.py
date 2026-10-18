#!/usr/bin/env python3
"""
Epistemica importer: Notion "Modelado" export -> notes corpus.

One-off migration tool. Reads the Notion export of the "Modelado"
(Modelling) area — the source knowledge base behind the epistemical
notes — and writes it into the notes corpus under
src/note/app/data/epistemica/:

  <export>/Modelado/<Domain>.md                  -> epistemica/<domain>.md
  <export>/Modelado/<Domain>/.../<Element>.md    -> epistemica/<domain>/<element>.md

- Every `.md` below `Modelado/` becomes a note. Direct children of
  `Modelado/` are the domain notes, written at the section root; all
  others are element notes, flattened into their domain directory
  ("Conceptual Model <Domain>" and deeper nesting collapse away).
- Titles come from the first `# ` heading (fallback: the filename with
  its 32-hex Notion suffix removed). Slugs follow the corpus naming rules
  (src/note/README.md): ASCII, lowercase, kebab-case; accent-folded;
  collisions get a numeric suffix.
- Each domain's base CSV (<Collection> <hash>.csv) is read for a
  `name,tags` mapping; matching entries get `tags: [...]` front matter.
  A Notion `tags:` property line in the body is merged in too.
- Notion noise is stripped: bare `: <number>` property lines,
  ellipsis-only (`> …`) placeholder blockquotes, and empty `## Index`
  headings. Everything else is kept verbatim.
- Referenced images are copied beside their note (assets/<slug>/) and
  their links rewritten to relative paths; unreferenced images are
  dropped.
- Notion page links to corpus notes are rewritten to relative targets;
  links to the collection CSVs collapse to their label; external links
  are left verbatim.
- Existing files are never overwritten: colliding targets are skipped
  with a warning — the corpus becomes the source of truth.

Run the indexer afterwards: python3 src/note/bin/index.py

Usage: python3 src/note/bin/import_epistemica.py <export-root>
"""

import argparse
import csv
import json
import posixpath
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import unquote

NOTE = Path(__file__).resolve().parent.parent
TARGET = NOTE / "app" / "data" / "epistemica"
CHANGELOG = NOTE / "app" / "data" / "changelog.json"

UUID_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}(?=\.md$)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
TAGS_LINE_RE = re.compile(r"^\s*tags:\s*(.*)$", re.IGNORECASE)
NOISE_NUMBER_RE = re.compile(r"^\s*:\s*\d+\s*$")
ELLIPSIS_QUOTE_RE = re.compile(r"^\s*>\s*(…|\.\.\.|…\s*…)\s*$")
IMG_RE = re.compile(
    r"!\[([^\]]*)\]\((.+?\.(?:png|jpe?g|gif|svg|webp))\)", re.IGNORECASE
)
LINK_RE = re.compile(
    r"(?<!!)\[([^\]]*)\]\(((?:[^()]|\([^()]*\))*?\.(?:md|csv|html)(?:#[^)]*)?)\)",
    re.IGNORECASE,
)
EXT_RE = re.compile(r"\.(png|jpe?g|gif|svg|webp)$", re.IGNORECASE)


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


def stem_of(path: Path) -> str:
    return UUID_SUFFIX_RE.sub("", path.stem)


def norm_tags(raw: str, tags: list) -> None:
    for part in raw.split(","):
        tag = kebab(part.strip().strip("'\""))
        if tag and tag not in tags:
            tags.append(tag)


def clean_body(md: str) -> tuple:
    """Strip Notion noise + a body `tags:` line; return (body, tags)."""
    tags: list = []
    lines = []
    for line in md.splitlines():
        m = TAGS_LINE_RE.match(line)
        if m:
            norm_tags(m.group(1), tags)
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


def load_csv_tags(modelado: Path) -> dict:
    """Merge every base (<Collection> <hash>.csv) name->tags map."""
    tags_by_name: dict = {}
    for path in sorted(modelado.rglob("*.csv")):
        if path.name.endswith("_all.csv"):
            continue
        try:
            with open(path, encoding="utf-8-sig", errors="replace", newline="") as f:
                rows = list(csv.reader(f))
        except OSError:
            continue
        for row in rows[1:]:
            if len(row) < 2:
                continue
            name = row[0].strip().lower()
            if not name:
                continue
            tags: list = []
            norm_tags(row[1], tags)
            if tags:
                tags_by_name.setdefault(name, tags)
    return tags_by_name


def assign_targets(sources: list, modelado: Path) -> tuple:
    """Map each source .md to a corpus-relative target path."""
    src_to_target: dict = {}
    dir_taken: dict = {}
    collisions: list = []
    for path in sources:
        rel = path.relative_to(modelado)
        md = path.read_text(encoding="utf-8", errors="replace")
        h1 = parse_h1(md, stem_of(path))
        base = slugify(h1) or slugify(stem_of(path)) or "untitled"
        if len(rel.parts) == 1:
            parent = Path(".")
        else:
            parent = Path(kebab(rel.parts[0]))
        taken = dir_taken.setdefault(parent.as_posix(), set())
        slug = free_slug(base, taken, collisions)
        src_to_target[rel.as_posix()] = (parent / f"{slug}.md").as_posix()
    return src_to_target, collisions


def resolve_link(target: str, note_rel: Path, src_to_target: dict):
    """Rewrite an internal link; return None to collapse it to its label."""
    decoded = unquote(target)
    path_part, sep, anchor = decoded.partition("#")
    if not path_part:
        return target
    if EXT_RE.search(path_part):
        return target
    internal = path_part.lower().endswith((".md", ".csv"))
    # Notion page links are export-root-relative; a few are note-relative.
    keys = set()
    for base in (Path(), note_rel.parent):
        keys.add(posixpath.normpath((base / path_part).as_posix()))
    if path_part.startswith("Modelado/"):
        keys.add(path_part[len("Modelado/"):])
    for key in keys:
        if key in src_to_target:
            return src_to_target[key] + (sep + anchor if sep else "")
    return None if internal else target


def migrate_images(md: str, note_path: Path, note_slug: str,
                   asset_dir: Path, warnings: list) -> tuple:
    """Copy referenced local images into asset_dir; rewrite their links."""
    copied = 0

    def fix(m):
        nonlocal copied
        alt, target = m.group(1), m.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            return m.group(0)
        src = note_path.parent / unquote(target)
        if not src.is_file():
            warnings.append(f"{note_slug} (missing image '{target}')")
            return m.group(0)
        stem = slugify(src.stem) or "image"
        ext = src.suffix.lower()
        name = f"{stem}{ext}"
        n = 2
        while (
            (asset_dir / name).exists()
            and (asset_dir / name).read_bytes() != src.read_bytes()
        ):
            name = f"{stem}-{n}{ext}"
            n += 1
        asset_dir.mkdir(parents=True, exist_ok=True)
        dest = asset_dir / name
        if not dest.exists():
            dest.write_bytes(src.read_bytes())
            copied += 1
        return f"![{alt}](assets/{note_slug}/{name})"

    return IMG_RE.sub(fix, md), copied


def rewrite_links(md: str, note_rel: Path, src_to_target: dict,
                  note_target_dir: str) -> str:
    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
            return m.group(0)
        new = resolve_link(target, note_rel, src_to_target)
        if new is None:
            return label
        if new != target:
            rel = posixpath.relpath(new.split("#", 1)[0], note_target_dir)
            if "#" in new:
                rel += "#" + new.split("#", 1)[1]
            new = rel
        return f"[{label}]({new})"

    return LINK_RE.sub(fix, md)


def update_changelog(new_entries: list) -> int:
    """Append one log per newly imported note; keep file_path key order."""
    data = []
    if CHANGELOG.exists():
        data = json.loads(CHANGELOG.read_text(encoding="utf-8"))
    known = {e.get("file_path") for e in data}
    added = 0
    for file_path, summary in sorted(new_entries):
        if file_path in known:
            continue
        data.append({
            "file_path": file_path,
            "logs": [{
                "date": date.today().isoformat(),
                "kind": "feat",
                "summary": summary,
            }],
        })
        known.add(file_path)
        added += 1
    data.sort(key=lambda e: e.get("file_path", ""))
    CHANGELOG.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return added


def emit_note(path: Path, rel: Path, target_rel: str, src_to_target: dict,
              tags_by_name: dict, warnings: list, skipped: list):
    """Write one note; return (title, images, untagged) or None if skipped."""
    dest = TARGET / target_rel
    if dest.exists():
        skipped.append(target_rel)
        return None

    md = path.read_text(encoding="utf-8", errors="replace")
    h1 = parse_h1(md, stem_of(path))
    body, body_tags = clean_body(md)

    tags = list(tags_by_name.get(h1.strip().lower(), []))
    for t in body_tags:
        if t not in tags:
            tags.append(t)
    if not tags:
        tags = list(tags_by_name.get(stem_of(path).strip().lower(), []))
        for t in body_tags:
            if t not in tags:
                tags.append(t)

    note_slug = dest.stem
    body, copied = migrate_images(
        body, path, note_slug, dest.parent / "assets" / note_slug, warnings
    )
    note_dir = dest.parent.relative_to(TARGET).as_posix()
    body = rewrite_links(body, rel, src_to_target, note_dir)

    dest.parent.mkdir(parents=True, exist_ok=True)
    if tags:
        text = "---\ntags: [%s]\n---\n\n%s" % (", ".join(tags), body)
    else:
        text = body
    dest.write_text(text, encoding="utf-8")
    return h1 or note_slug, copied, not tags


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import a Notion 'Modelado' export into the epistemica "
                    "notes corpus."
    )
    parser.add_argument("export_root", help="dir containing Modelado/")
    args = parser.parse_args()

    export_root = Path(args.export_root)
    modelado = export_root / "Modelado"
    if not modelado.is_dir():
        print(f"ERROR: {modelado} not found", file=sys.stderr)
        return 1

    sources = sorted(modelado.rglob("*.md"))
    if not sources:
        print(f"ERROR: no .md under {modelado}", file=sys.stderr)
        return 1
    root_notes = sorted(export_root.glob("Modelado *.md"))

    src_to_target, collisions = assign_targets(sources, modelado)
    tags_by_name = load_csv_tags(modelado)
    TARGET.mkdir(parents=True, exist_ok=True)

    warnings: list = []
    skipped: list = []
    imported = 0
    images = 0
    untagged = 0
    changelog_entries: list = []

    for path in sources:
        rel = path.relative_to(modelado)
        target_rel = src_to_target[rel.as_posix()]
        res = emit_note(path, rel, target_rel, src_to_target, tags_by_name,
                        warnings, skipped)
        if res is None:
            continue
        title, copied, no_tags = res
        imported += 1
        images += copied
        untagged += no_tags
        changelog_entries.append((
            f"epistemica/{target_rel}",
            f"Import {title} from the Modelado Notion export.",
        ))

    for rp in root_notes:
        rel = Path(rp.name)
        res = emit_note(rp, rel, "modelado.md", src_to_target, tags_by_name,
                        warnings, skipped)
        if res is None:
            continue
        title, copied, no_tags = res
        imported += 1
        images += copied
        untagged += no_tags
        changelog_entries.append((
            "epistemica/modelado.md",
            f"Import {title} from the Modelado Notion export.",
        ))

    logs_added = update_changelog(changelog_entries)

    total = len(sources) + len(root_notes)
    print(f"epistemica-import: {total} files -> {imported} notes "
          f"({len(skipped)} skipped, {images} images, {untagged} untagged, "
          f"{logs_added} changelog logs)")
    if collisions:
        print(f"slug collisions (suffixed): {len(collisions)}")
        for c in collisions:
            print(f"  ! {c}")
    if skipped:
        print(f"skipped (target exists): {len(skipped)}")
        for s in skipped:
            print(f"  - {s}")
    if warnings:
        print(f"warnings: {len(warnings)}")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
