#!/usr/bin/env python3
"""Build the unified library index.

Merges the three corpus indexes into one lightweight metadata file,
src/app/data/library-index.json, consumed by the hub and the unified
library page. Each entry keeps {corpus, kind, path, title, section,
tags, words}; full text stays in the per-corpus indexes. The notes
index's `links` registry (data/links.json, embedded by notes_index.py)
is carried through so the explorer renders its linked group.

Usage: python3 bin/build_library_index.py
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from indexlib import Progress, atomic_write_text, run_builder

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "src" / "app" / "data" / "library-index.json"

SOURCES = [
    ("note", REPO / "src" / "app" / "data" / "notes-index.json", "notes"),
    ("document", REPO / "src" / "app" / "data" / "documents-index.json", "documents"),
    ("course", REPO / "src" / "app" / "data" / "courses-index.json", "entries"),
]


def load(path: Path, key: str):
    if not path.exists():
        raise SystemExit(f"ERROR: missing index {path} — run make index first")
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get(key, []), data.get("links", [])


def build(progress=None) -> bool:
    if progress is not None:
        progress.start("merging the corpus indexes")

    entries = []
    links = []
    for corpus, path, key in SOURCES:
        items, corpus_links = load(path, key)
        if corpus == "note":
            links = corpus_links
        for item in items:
            prefix = {"note": "notes", "document": "documents", "course": "courses"}[corpus]
            entry = {
                "corpus": corpus,
                "kind": item.get("kind", corpus),
                "path": prefix + "/" + item.get("path", ""),
                "title": item.get("title", ""),
                "section": item.get("section") or corpus,
                "tags": item.get("tags", []),
                "words": item.get("words", 0),
            }
            if item.get("course"):
                entry["course"] = prefix + "/" + item["course"]
            if item.get("order") is not None:
                entry["order"] = item["order"]
            entries.append(entry)
        if progress is not None:
            progress.step(len(items), message=f"{corpus} merged")

    order = {"note": 0, "document": 1, "course": 2}
    entries.sort(key=lambda e: (order.get(e["corpus"], 9), e["path"]))
    counts = Counter(e["corpus"] for e in entries)
    sections = {}
    for e in entries:
        sections.setdefault(e["corpus"], Counter())[e["section"]] += 1

    if progress is not None:
        progress.stage(f"writing {OUT.name}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(OUT, json.dumps({
        "generated": date.today().isoformat(),
        "count": len(entries),
        "kinds": dict(counts),
        "sections": {k: dict(v) for k, v in sections.items()},
        "links": links,
        "entries": entries,
    }, ensure_ascii=False, separators=(",", ":")))

    kb = OUT.stat().st_size / 1024
    print(f"library-index: {len(entries)} entries, {len(links)} links "
          f"-> src/app/data/library-index.json ({kb:.0f} KB)")
    for corpus, count in sorted(counts.items()):
        print(f"  {corpus}: {count}")
    if progress is not None:
        progress.finish(f"{len(entries)} entries")
    return True


def main() -> int:
    return run_builder("library", build)


if __name__ == "__main__":
    raise SystemExit(main())
