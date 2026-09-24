#!/usr/bin/env python3
"""
Universal search index builder (prototype).

Merges the per-corpus search indexes plus a snapshot of both ontology
node sets into one committed file, src/app/data/search-index.json,
consumed by the hub search box (/). Stdlib only.

- Corpora (no backend needed): notes, courses, documents,
  glossarium — trimmed to {surface, kind, type, title, path, tags,
  excerpt} so the page fetches one ~2 MB file instead of ~4 MB of
  full-text indexes. Ranking beyond the excerpt stays in the
  per-catalog indexes; the universal box links out to them.
- Graph nodes: pulled live from CouchDB (same shaping as the
  /{ds}/api/nodes endpoints: layout doc excluded, _id/_rev stripped),
  trimmed to {surface, kind "node", type category|layer, title name,
  path id, excerpt short_description}. When CouchDB is unreachable the
  committed app/data/data.json seeds are used instead and the payload
  records "snapshot_source": "seed" (a build-time snapshot is not the
  live API, so this does not break the no-fallback contract — and the
  marker makes staleness visible).

The corpus indexes must exist first (make notes-index course-index
document-index glossarium-index); missing ones abort the
build with a hint. Regenerate deliberately before build/deploy — the
file is committed, like the per-corpus indexes.

Usage: python3 bin/build_search_index.py
"""

import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couchdb_client  # noqa: E402
import envutil  # noqa: E402

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

    gloss = load_index(app / "glossarium" / "app" / "data" / "index.json",
                       "make glossarium-index")
    for n in gloss.get("terms", []):
        aliases = n.get("aliases", [])
        if isinstance(aliases, str):
            try:
                aliases = json.loads(aliases)
            except ValueError:
                aliases = []
        entries.append({
            "surface": "glossarium",
            "kind": "term",
            "type": "",
            "title": n.get("name", ""),
            "path": n.get("slug", ""),
            "tags": [],
            "aliases": aliases if isinstance(aliases, list) else [],
            "excerpt": excerpt(n.get("excerpt") or n.get("text", "")),
        })

    return entries


def live_nodes(cfg, surface: str) -> list:
    """Node snapshot from CouchDB, shaped like the /api/nodes endpoint."""
    docs = couchdb_client.all_docs(cfg)
    out = []
    for doc in docs:
        if not isinstance(doc, dict):
            continue
        if doc.get("_id") == "layout" or doc.get("type") == "layout":
            continue
        node = {k: v for k, v in doc.items() if k not in ("_id", "_rev")}
        out.append({
            "surface": surface,
            "kind": "node",
            "type": node.get("category") or node.get("layer") or "",
            "title": node.get("name") or node.get("id") or "",
            "path": node.get("id") or "",
            "tags": [],
            "excerpt": excerpt(node.get("short_description") or ""),
        })
    return out


def seed_nodes(app_name: str, surface: str) -> list:
    raw = json.loads(
        (REPO / "src" / app_name / "app" / "data" / "data.json")
        .read_text(encoding="utf-8")
    )
    docs = raw if isinstance(raw, list) else raw.get("nodes", [])
    out = []
    for doc in docs:
        if not isinstance(doc, dict):
            continue
        if doc.get("_id") == "layout" or doc.get("type") == "layout":
            continue
        node = {k: v for k, v in doc.items() if k not in ("_id", "_rev")}
        out.append({
            "surface": surface,
            "kind": "node",
            "type": node.get("category") or node.get("layer") or "",
            "title": node.get("name") or node.get("id") or "",
            "path": node.get("id") or "",
            "tags": [],
            "excerpt": excerpt(node.get("short_description") or ""),
        })
    return out


def main() -> int:
    entries = corpus_entries()

    snapshot_source = "couchdb"
    node_entries = []
    try:
        for app_name, surface, env_key, default_db in (
            ("epistemica", "epistemica", "EPISTEMICA_DB", "epistemica"),
            ("tecnica", "tecnica", "TECNICA_DB", "tecnica"),
        ):
            cfg = envutil.dataset(env_key, default_db)
            node_entries.extend(live_nodes(cfg, surface))
    except Exception as exc:
        print(f"search-index: CouchDB unavailable ({exc}) — using seed snapshots")
        snapshot_source = "seed"
        node_entries = seed_nodes("epistemica", "epistemica") + \
            seed_nodes("tecnica", "tecnica")

    entries.extend(node_entries)

    counts = {}
    for e in entries:
        counts[e["surface"]] = counts.get(e["surface"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "generated": date.today().isoformat(),
        "snapshot_source": snapshot_source,
        "counts": counts,
        "entries": entries,
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    print(f"search-index: {len(entries)} entries ({snapshot_source} nodes) -> "
          f"src/app/data/search-index.json ({kb:.0f} KB)")
    for surface, count in sorted(counts.items()):
        print(f"  {surface}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
