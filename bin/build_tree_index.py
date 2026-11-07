#!/usr/bin/env python3
"""Build the corpus name index: a directory tree plus a flat searchable name list.

The tree page is a *directory/name* search — it matches folder names and file
titles, never content or tags — so this file carries only what that needs:

  nodes:  dir path -> { n: name, p: parent, d: [child dirs], c: count }
  files:  [ { p: path, n: lowercase title, t: title, k: kind, e: ext } ]
          sorted by n, so a prefix query is a binary search

`path` is stored once per file; the directory is derivable from it.

Output: src/app/data/tree-index.json

Usage: python3 bin/build_tree_index.py
"""
import json
from datetime import date
from pathlib import Path

from indexlib import Progress, atomic_write_text, run_builder

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "src" / "app" / "data" / "tree-index.json"
SRC = REPO / "src" / "app" / "data" / "library-index.json"

ROOT_ORDER = {"notes": 0, "documents": 1, "courses": 2}


def build(progress=None):
    if not SRC.exists():
        raise SystemExit(f"ERROR: missing {SRC} — run: make library-index")

    if progress is not None:
        progress.start("reading the library index")

    entries = json.loads(SRC.read_text(encoding="utf-8")).get("entries", [])
    if progress is not None:
        progress.set_total(len(entries))

    nodes = {"": {"n": "", "p": None, "d": [], "c": 0}}
    files = []

    for i, e in enumerate(entries):
        path = (e.get("path") or "").strip()
        if not path:
            continue
        parts = path.split("/")
        kind = e.get("kind") or e.get("corpus") or "note"

        # a course entry is the directory itself, not a file in it
        if kind == "course":
            dir_parts = parts
        else:
            dir_parts = parts[:-1]

        acc = ""
        for seg in dir_parts:
            nxt = (acc + "/" + seg) if acc else seg
            if nxt not in nodes:
                nodes[nxt] = {"n": seg, "p": acc, "d": [], "c": 0}
                nodes[acc]["d"].append(seg)
            acc = nxt

        nodes[acc]["c"] += 1
        chain = acc
        while chain:
            parent = nodes[chain]["p"]
            if parent is None:
                break
            nodes[parent]["c"] += 1
            chain = parent

        if kind == "course":
            files.append({
                "p": path + "/readme.md",
                "n": (e.get("title") or parts[-1]).lower(),
                "t": e.get("title") or parts[-1],
                "k": "course",
                "e": "md",
            })
            continue

        title = e.get("title") or parts[-1].rsplit(".", 1)[0]
        ext = path.rsplit(".", 1)[-1].lower() if "." in path else "md"
        files.append({
            "p": path,
            "n": str(title).lower(),
            "t": title,
            "k": kind,
            "e": ext,
        })

        if progress is not None and i and i % 2000 == 0:
            progress.step(2000, message="building the name index")

    for node in nodes.values():
        node["d"].sort(key=str.lower)

    # the synthetic root lists the corpora it contains
    roots = sorted([d for d, n in nodes.items() if n["p"] == "" and d],
                   key=lambda d: (ROOT_ORDER.get(d, 9), d))
    nodes[""]["d"] = roots

    files.sort(key=lambda f: (f["n"], f["p"]))

    payload = {
        "generated": date.today().isoformat(),
        "count": len(files),
        "dirs": len(nodes) - 1,
        "roots": roots,
        "nodes": nodes,
        "files": files,
    }

    if progress is not None:
        progress.stage(f"writing {OUT.name}")

    atomic_write_text(OUT, json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    kb = OUT.stat().st_size / 1024
    print(f"tree-index: {payload['count']} files, {payload['dirs']} dirs -> "
          f"src/app/data/tree-index.json ({kb:.0f} KB)")
    if progress is not None:
        progress.finish(f"{payload['count']} files")
    return True


def main():
    return run_builder("tree", build)


if __name__ == "__main__":
    raise SystemExit(main())
