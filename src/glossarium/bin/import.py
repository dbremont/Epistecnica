#!/usr/bin/env python3
"""
Glossarium importer: Notion export -> corpus.

One-off migration tool. Reads a Notion export directory (the "Glosarium"
database export: a `Glosarium/` folder of per-term markdown files named
"<Term> <32-hex-uuid>.md", plus the database CSVs) and writes the
glossarium corpus: one <slug>.md per term under src/glossarium/app/terms/.

- The original term name is preserved as the markdown H1 (fallback: the
  filename without the uuid suffix).
- Notion property noise (bare ": <number>" lines) is stripped; everything
  else is kept verbatim — the corpus becomes the source of truth.
- English translations found in the export CSV (the `english` column) are
  embedded as `aliases:` front matter so the selection-lookup can match
  across languages.
- Slugs follow the corpus naming rules (see src/glossarium/README.md):
  ASCII, lowercase, kebab-case; accent-folded; uuid suffixes removed;
  collisions get a numeric suffix.

Run the indexer afterwards: python3 src/glossarium/bin/index.py

Usage: python3 src/glossarium/bin/import.py <notion-export-dir>
"""

import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

GLOSSARIUM = Path(__file__).resolve().parent.parent
TERMS = GLOSSARIUM / "app" / "terms"

UUID_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}(?=\.md$)")
NOISE_LINE_RE = re.compile(r"^\s*:\s*\d+\s*$")
# `english: <translation>` property lines duplicate the CSV aliases that
# already land in front matter.
ENGLISH_LINE_RE = re.compile(r"^\s*english:\s*\S.*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_ALIASES_RE = re.compile(r"^aliases:\s*\[(.*)\]\s*$")
# Notion-internal links: [text](Some%20Name%20<uuid>.md) — targets may nest
# one level of parens ("Peso (Moneda)"). Applied before the bare-mention
# form so rewritten links are not double-processed.
MD_LINK_RE = re.compile(
    r"\[([^\]]*)\]\((?:[^()]|\([^()]*\))*(?:%20|\s)[0-9a-f]{32}\.md\)"
)
UUID_IN_LINK_RE = re.compile(r"([0-9a-f]{32})\.md\)$")
BARE_MENTION_RE = re.compile(
    r"\s?\((?:[^()\[\]]|\([^()\[\]]*\))*(?:%20|\s)[0-9a-f]{32}\.md\)"
)


def slugify(name: str) -> str:
    folded = unicodedata.normalize("NFKD", name)
    folded = folded.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")
    return slug


def free_path(directory: Path, slug: str) -> Path:
    candidate = directory / f"{slug}.md"
    n = 2
    while candidate.exists():
        candidate = directory / f"{slug}-{n}.md"
        n += 1
    return candidate


def load_aliases(export_dir: Path) -> dict:
    """name -> english translation, from the export CSV `english` column."""
    aliases = {}
    for csv_path in sorted(export_dir.glob("*.csv")):
        try:
            with open(csv_path, encoding="utf-8-sig", newline="") as fh:
                reader = csv.DictReader(fh)
                if not reader.fieldnames or "english" not in reader.fieldnames:
                    continue
                for row in reader:
                    name = (row.get("name") or "").strip()
                    english = (row.get("english") or "").strip()
                    if name and english and english.lower() != name.lower():
                        aliases.setdefault(name, english)
        except (OSError, csv.Error) as exc:
            print(f"  ! csv skipped ({csv_path.name}): {exc}", file=sys.stderr)
    return aliases


def split_front_matter(md: str):
    """Existing `aliases: [...]` front matter, if any; (aliases, body)."""
    aliases, rest = [], md
    if md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) == 3:
            for line in parts[1].splitlines():
                m = FRONT_MATTER_ALIASES_RE.match(line.strip())
                if m:
                    aliases = [
                        a.strip().strip("'\"")
                        for a in m.group(1).split(",")
                        if a.strip()
                    ]
            rest = parts[2].lstrip("\n")
    return aliases, rest


def parse_term(path: Path):
    """(name, body) with noise stripped; name from the H1, else filename."""
    md = path.read_text(encoding="utf-8", errors="replace")
    aliases, md = split_front_matter(md)

    name = None
    body_lines = []
    for line in md.splitlines():
        if NOISE_LINE_RE.match(line) or ENGLISH_LINE_RE.match(line):
            continue
        if name is None:
            m = HEADING_RE.match(line)
            if m and len(m.group(1)) == 1:
                name = m.group(2).strip()
                continue
        body_lines.append(line)

    if name is None:
        name = UUID_SUFFIX_RE.sub("", path.name)[:-3].strip()
    while body_lines and not body_lines[-1].strip():
        body_lines.pop()

    return name, aliases, "\n".join(body_lines).strip("\n")


def render(name: str, aliases, body: str) -> str:
    front = ""
    if aliases:
        joined = ", ".join(a.replace("'", "\\'") for a in aliases)
        front = "---\naliases: [%s]\n---\n" % joined
    return f"{front}# {name}\n\n{body}\n"


def rewrite_links(body: str, slug_by_uuid: dict) -> str:
    """Notion-internal links -> glossarium term links (unknown uuids: unlink)."""

    def md_link(m):
        text, uuid = m.group(1), UUID_IN_LINK_RE.search(m.group(0))
        slug = slug_by_uuid.get(uuid.group(1)) if uuid else None
        if slug:
            return f"[{text}](index.html?t={slug})"
        return text

    body = MD_LINK_RE.sub(md_link, body)
    return BARE_MENTION_RE.sub("", body)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="import.py",
        description="Import a Notion Glosarium export into the glossarium corpus.",
    )
    parser.add_argument("export_dir", type=Path, help="Notion export directory")
    args = parser.parse_args()

    export_dir = args.export_dir
    term_dirs = [d for d in export_dir.iterdir() if d.is_dir()] if export_dir.is_dir() else []
    if not term_dirs:
        print(f"ERROR: no term directory found inside {export_dir}", file=sys.stderr)
        return 1

    TERMS.mkdir(parents=True, exist_ok=True)
    aliases_by_name = load_aliases(export_dir)

    # Pass 1: parse every term (name, aliases, noise-free body).
    parsed, warnings = [], []
    for path in sorted(term_dirs[0].glob("*.md")):
        name, aliases, body = parse_term(path)
        if not body:
            warnings.append(f"{path.name}: empty body")
        extra = aliases_by_name.get(name)
        if extra and extra not in aliases:
            aliases.append(extra)
        slug = slugify(name)
        if not slug:
            warnings.append(f"{path.name}: slug is empty")
            continue
        uuid = UUID_SUFFIX_RE.search(path.name)
        parsed.append(
            {
                "name": name,
                "aliases": aliases,
                "body": body,
                "slug": slug,
                "uuid": uuid.group(0).strip() if uuid else None,
            }
        )

    slug_by_uuid = {p["uuid"]: p["slug"] for p in parsed if p["uuid"]}

    # Pass 2: rewrite Notion links, resolve slug collisions, write.
    imported, alias_count = 0, 0
    for term in parsed:
        term["body"] = rewrite_links(term["body"], slug_by_uuid)
        alias_count += len(term["aliases"])

        out = free_path(TERMS, term["slug"])
        if out.stem != term["slug"]:
            warnings.append(f"{term['name']!r}: slug collision -> {out.stem}")
        out.write_text(render(term["name"], term["aliases"], term["body"]), encoding="utf-8")
        imported += 1

    print(f"glossarium-import: {imported} terms, {alias_count} aliases -> {TERMS}")
    for warning in warnings:
        print(f"  ! {warning}")
    print("next: python3 src/glossarium/bin/index.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
