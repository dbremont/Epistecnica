#!/usr/bin/env python3
"""
Universal search index builder (prototype).

Merges the per-corpus search indexes into one committed file,
src/app/data/search-index.json, consumed by the hub search box (/) and the
per-catalog boxes. Stdlib only.

- Corpora (no backend needed): notes, courses, documents
  — trimmed to {surface, kind, type, title, path, tags,
  excerpt} so the page fetches one ~2 MB file instead of ~4 MB of
  full-text indexes. Ranking beyond the excerpt stays in the
  per-catalog indexes; the universal box links out to them.
- The ontology graphs are external (Naturgnosis spaces) and are not
  indexed here; their former node snapshots were dropped when the local
  graph apps were retired.

The corpus indexes must exist first (make notes-index course-index
document-index); missing ones abort the
build with a hint. Regenerate deliberately before build/deploy — the
file is committed, like the per-corpus indexes.

Usage: python3 bin/build_search_index.py
"""

import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "src" / "app" / "data" / "search-index.json"

EXCERPT_LEN = 500


def excerpt(text: str) -> str:
    text = " ".join((text or "").split())
    if len(text) <= EXCERPT_LEN:
        return text
    cut = text[:EXCERPT_LEN]
    space = cut.rfind(" ")
    return (cut[:space] if space > 40 else cut).rstrip() + " …"


def load_index(path: Path, hint: str) -> dict:
    if not path.is_file():
        print(f"ERROR: missing index {path} — run: {hint}", file=sys.stderr)
        raise SystemExit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def corpus_entries() -> list:
    entries = []
    app = REPO / "src"

    notes = load_index(app / "note" / "app" / "data" / "index.json",
                       "make notes-index")
    for n in notes.get("notes", []):
        entries.append({
            "surface": "note",
            "kind": n.get("kind", "note"),
            "type": n.get("section", ""),
            "title": n.get("title", ""),
            "path": n.get("path", ""),
            "tags": n.get("tags", []),
            "excerpt": excerpt(n.get("text", "")),
        })

    courses = load_index(app / "course" / "app" / "data" / "index.json",
                         "make course-index")
    for n in courses.get("entries", []):
        entries.append({
            "surface": "course",
            "kind": n.get("kind", ""),
            "type": n.get("course", ""),
            "title": n.get("title", ""),
            "path": n.get("path", ""),
            "tags": n.get("tags", []),
            "excerpt": excerpt(n.get("text", "")),
        })

    documents = load_index(app / "document" / "app" / "data" / "index.json",
                           "make document-index")
    for n in documents.get("documents", []):
        entries.append({
            "surface": "document",
            "kind": "document",
            "type": n.get("section", ""),
            "title": n.get("title", ""),
            "path": n.get("path", ""),
            "tags": n.get("tags", []),
            "excerpt": excerpt(n.get("text", "")),
        })

    return entries


def main() -> int:
    entries = corpus_entries()

    counts = {}
    for e in entries:
        counts[e["surface"]] = counts.get(e["surface"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "generated": date.today().isoformat(),
        "counts": counts,
        "entries": entries,
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    print(f"search-index: {len(entries)} entries -> "
          f"src/app/data/search-index.json ({kb:.0f} KB)")
    for surface, count in sorted(counts.items()):
        print(f"  {surface}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
