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

from indexlib import Progress, atomic_write_text, run_builder

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

    notes = load_index(app / "app" / "data" / "notes-index.json",
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

    courses = load_index(app / "app" / "data" / "courses-index.json",
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

    documents = load_index(app / "app" / "data" / "documents-index.json",
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

    # Optional corpora: indexed when present, skipped otherwise (a partial
    # `make index --only search` still works).
    gloss = app / "glossarium" / "app" / "data" / "index.json"
    if gloss.is_file():
        for t in json.loads(gloss.read_text(encoding="utf-8")).get("terms", []):
            entries.append({
                "surface": "glossarium",
                "kind": "term",
                "type": "term",
                "title": t.get("name", ""),
                "path": t.get("slug", ""),
                "tags": [],
                "excerpt": t.get("excerpt", ""),
            })

    qa = app / "qa" / "app" / "data" / "qa-index.json"
    if qa.is_file():
        for e in json.loads(qa.read_text(encoding="utf-8")).get("entries", []):
            entries.append({
                "surface": "qa",
                "kind": "qa",
                "type": e.get("status", "open"),
                "title": e.get("question", ""),
                "path": e.get("id", ""),
                "tags": e.get("tags", []),
                "excerpt": e.get("excerpt", ""),
            })

    return entries


def build(progress=None) -> bool:
    if progress is not None:
        progress.start("merging the corpus indexes")
    entries = corpus_entries()
    if progress is not None:
        progress.set_total(len(entries))
        progress.step(len(entries), message="entries merged")

    counts = {}
    for e in entries:
        counts[e["surface"]] = counts.get(e["surface"], 0) + 1

    if progress is not None:
        progress.stage(f"writing {OUT.name}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(OUT, json.dumps({
        "generated": date.today().isoformat(),
        "counts": counts,
        "entries": entries,
    }, ensure_ascii=False, separators=(",", ":")))

    kb = OUT.stat().st_size / 1024
    print(f"search-index: {len(entries)} entries -> "
          f"src/app/data/search-index.json ({kb:.0f} KB)")
    for surface, count in sorted(counts.items()):
        print(f"  {surface}: {count}")
    if progress is not None:
        progress.finish(f"{len(entries)} entries")
    return True


def main() -> int:
    return run_builder("search", build)


if __name__ == "__main__":
    raise SystemExit(main())
