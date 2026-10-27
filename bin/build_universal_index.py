#!/usr/bin/env python3
"""
Universal graph index builder (Epistecnica hub).

Replicates the *concept* of the Naturgnosis universal view ("Graphive"): one
view-only canvas over everything we hold. Unlike Naturgnosis — whose nodes are
graph-space datasets — here the graph is generated from Epistecnica's own
content:

    notes      src/note/app/data/index.json      (+ the links registry)
    courses    src/course/app/data/index.json
    documents  src/document/app/data/index.json
    ees       src/note/app/data/epistemica/ees.json

Nodes are namespaced ``uid = "{surface}:{id}"``. Edges are:

    structural   notes links.json "related" pairs (chained — its `from` is a
                 directory, not a node), course -> lecture, EES parent -> child
    shared tags  within each tag, members are chained (bounded, deterministic)

Outputs (hub-owned, like app/data/search-index.json):

    src/app/graph/data/universal-graph.json   {generated, snapshot_source,
                                               counts, edge_counts, nodes}
    src/app/graph/data/universal-layout.json  {uid: [x, y]} (bin/layout.py)

The viewer at src/app/graph/index.html fetches both relatively (`data/...`)
and renders them with the vendored deck.gl renderer. Stdlib only.

Usage: python3 bin/build_universal_index.py
"""

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent

NOTE_INDEX = REPO / "src" / "note" / "app" / "data" / "index.json"
LINKS_FILE = REPO / "src" / "note" / "app" / "data" / "links.json"
COURSE_INDEX = REPO / "src" / "course" / "app" / "data" / "index.json"
DOCUMENT_INDEX = REPO / "src" / "document" / "app" / "data" / "index.json"
EES_TREE = REPO / "src" / "note" / "app" / "data" / "epistemica" / "ees.json"

OUT_DIR = REPO / "src" / "app" / "graph" / "data"
GRAPH_OUT = OUT_DIR / "universal-graph.json"

EXCERPT_LEN = 500

SOURCES = ("note", "course", "document", "ees")


def excerpt(text):
    text = " ".join((text or "").split())
    if len(text) <= EXCERPT_LEN:
        return text
    cut = text[:EXCERPT_LEN]
    space = cut.rfind(" ")
    if space > EXCERPT_LEN * 0.6:
        cut = cut[:space]
    return cut + "\u2026"


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def build_nodes():
    nodes = []

    # ---- notes -----------------------------------------------------------
    for n in load(NOTE_INDEX).get("notes", []):
        path = n["path"]
        nodes.append({
            "uid": "note:" + path,
            "source": "note",
            "source_id": path,
            "name": n.get("title") or path,
            "category": n.get("section") or "note",
            "layer": n.get("kind") or "",
            "tags": list(n.get("tags") or []),
            "description": excerpt(n.get("text")),
            "references": [],
            "deep_link": "/note/note.html?n=" + quote(path, safe="/"),
            "targets": [],
        })

    # ---- courses / lectures ---------------------------------------------
    for e in load(COURSE_INDEX).get("entries", []):
        path = e["path"]
        kind = e.get("kind") or "course"
        nodes.append({
            "uid": "course:" + path,
            "source": "course",
            "source_id": path,
            "name": e.get("title") or path,
            "category": kind,
            "layer": e.get("course") or "",
            "tags": list(e.get("tags") or []),
            "description": excerpt(e.get("text")),
            "references": [],
            "deep_link": ("/course/lecture.html?l=" + quote(path, safe="/"))
            if kind == "lecture"
            else ("/course/courses/" + quote(path, safe="/"))
            if kind == "live"
            else ("/course/course.html?c=" + quote(path, safe="/")),
            "targets": [],
        })

    # ---- documents -------------------------------------------------------
    for d in load(DOCUMENT_INDEX).get("documents", []):
        path = d["path"]
        nodes.append({
            "uid": "document:" + path,
            "source": "document",
            "source_id": path,
            "name": d.get("title") or path,
            "category": d.get("section") or "document",
            "layer": d.get("kind") or "",
            "tags": list(d.get("tags") or []),
            "description": excerpt(d.get("text")),
            "references": [],
            "deep_link": "/document/document.html?d=" + quote(path, safe="/"),
            "targets": [],
        })

    # ---- ees ------------------------------------------------------------
    ees_edges = []

    def walk_ees(node, parent_path):
        path = parent_path + [node.get("label") or ""]
        path_str = " \u2192 ".join(path)
        uid = "ees:" + path_str
        nodes.append({
            "uid": uid,
            "source": "ees",
            "source_id": path_str,
            "name": node.get("label") or path_str,
            "category": node.get("type") or "element",
            "layer": node.get("order") or "",
            "tags": [],
            "description": excerpt(node.get("description")),
            "references": [],
            "deep_link": "/note/data/epistemica/ees.html?node=" + quote(path_str),
            "targets": [],
        })
        for child in node.get("children", []):
            child_uid = "ees:" + " \u2192 ".join(path + [child.get("label") or ""])
            ees_edges.append((uid, child_uid))
            walk_ees(child, path)

    for root in load(EES_TREE).get("roots", []):
        walk_ees(root, [])

    by_uid = {n["uid"]: n for n in nodes}

    def add_edge(a, b):
        if a == b:
            return
        src = by_uid.get(a)
        if src is None or b not in by_uid or b in src["targets"]:
            return
        src["targets"].append(b)

    # ---- structural edges ------------------------------------------------
    for a, b in ees_edges:
        add_edge(a, b)

    # notes links.json: `from` is a directory; chain the `to` notes per `from`.
    if LINKS_FILE.exists():
        by_from = {}
        for lk in load(LINKS_FILE).get("links", []):
            if not isinstance(lk, dict):
                continue
            to = lk.get("to")
            if not isinstance(to, str):
                continue
            uid = "note:" + to
            if uid in by_uid:
                by_from.setdefault(lk.get("from") or "", []).append(uid)
        for members in by_from.values():
            for i in range(len(members) - 1):
                add_edge(members[i], members[i + 1])

    # course -> lecture
    for n in nodes:
        if n["source"] == "course" and n["category"] == "lecture" and n["layer"]:
            add_edge(n["uid"], "course:" + n["layer"])

    # ---- shared tags: chain members within each tag ----------------------
    by_tag = {}
    for n in nodes:
        for tag in n["tags"]:
            by_tag.setdefault(tag, []).append(n["uid"])
    for members in by_tag.values():
        members = sorted(set(members))
        for i in range(len(members) - 1):
            add_edge(members[i], members[i + 1])

    return nodes


def main():
    nodes = build_nodes()

    counts = {s: 0 for s in SOURCES}
    edge_counts = {s: 0 for s in SOURCES}
    for n in nodes:
        counts[n["source"]] = counts.get(n["source"], 0) + 1
        edge_counts[n["source"]] = edge_counts.get(n["source"], 0) + len(n["targets"])

    graph = {
        "generated": date.today().isoformat(),
        "snapshot_source": "epistecnica corpus (notes, courses, documents, ees)",
        "counts": counts,
        "edge_counts": edge_counts,
        "nodes": nodes,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(GRAPH_OUT, "w", encoding="utf-8") as fh:
        json.dump(graph, fh, ensure_ascii=False, separators=(",", ":"))

    total_edges = sum(edge_counts.values())
    size_kb = GRAPH_OUT.stat().st_size / 1024
    print(
        "universal-index: %d nodes (%s), %d edges -> %s (%.0f KB)"
        % (
            len(nodes),
            ", ".join("%s %d" % (s, counts.get(s, 0)) for s in SOURCES),
            total_edges,
            GRAPH_OUT.relative_to(REPO),
            size_kb,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
