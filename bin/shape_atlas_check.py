#!/usr/bin/env python3
"""
Geometric Shape Atlas store validator.

Validates src/corpus/notes/epistemica/mathematical/geometry/atlas.json:
the top-level metadata, the family and dimension vocabularies, the unique
tree paths and ids, the parent/family/dimension consistency, the figure
specification of every node, and the corpus-note links.  Stdlib only.

Usage: python3 bin/shape_atlas_check.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "src" / "corpus" / "notes"
STORE = NOTES / "epistemica" / "mathematical" / "geometry" / "atlas.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TOP_KEYS = (
    "title", "abbr", "version", "generated", "subtitle", "intro",
    "source", "note", "families", "dimensions", "stats", "roots",
)
COLORS = {
    "--accent-gold", "--accent-cyan", "--accent-violet", "--accent-copper",
    "--accent-copper-light", "--accent-sage", "--accent-plum", "--accent-rose",
    "--accent-amber", "--accent-steel",
}
KINDS = {"root", "family", "shape", "property"}
FIGURE_KINDS = {
    "annulus", "arc", "arrangement", "ball", "cardioid", "circle", "curve",
    "disk", "ellipse", "family", "fractal", "helix", "hyperplane",
    "hypersphere", "lens", "line", "n-torus", "parabolic-region", "plane",
    "point", "polygon", "polyhedron", "polyline", "polytope", "property",
    "quadric", "quadrilateral", "ray", "sector", "segment", "segment-region",
    "spiral", "spline", "surface", "torus", "triangle", "generic",
}
DIMENSION_IDS = {
    "degenerate", "1d", "2d", "curved-2d", "3d", "nd", "mixed", "property",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def walk(node: dict, depth: int = 1):
    yield node, depth
    for child in node.get("children", []):
        yield from walk(child, depth + 1)


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def main() -> int:
    errors: list[str] = []
    if not STORE.is_file():
        print(f"[shape-atlas] missing store: {STORE}", file=sys.stderr)
        return 1

    try:
        data = json.loads(STORE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[shape-atlas] invalid JSON: {exc}", file=sys.stderr)
        return 1
    if not isinstance(data, dict):
        print("[shape-atlas] store must be a JSON object", file=sys.stderr)
        return 1

    for key in TOP_KEYS:
        if key not in data:
            fail(errors, f"missing top-level key {key!r}")
    if errors:
        print("\n".join("[shape-atlas] " + e for e in errors), file=sys.stderr)
        return 1

    for key in ("title", "abbr", "subtitle", "intro", "source", "note"):
        if not nonempty(data.get(key)):
            fail(errors, f"{key} must be a non-empty string")
    for key in ("version", "generated"):
        if not isinstance(data.get(key), str) or not DATE_RE.match(data[key]):
            fail(errors, f"{key} must be YYYY-MM-DD")

    root_note = data.get("note")
    if nonempty(root_note):
        rel = Path(root_note)
        if rel.is_absolute() or ".." in rel.parts:
            fail(errors, "note must be relative to src/corpus/notes")
        elif rel.suffix not in (".md", ".html"):
            fail(errors, "note must end in .md or .html")
        elif not (NOTES / rel).is_file():
            fail(errors, f"note does not exist: {root_note}")

    families = data.get("families")
    if not isinstance(families, list) or not families:
        fail(errors, "families must be a non-empty list")
        families = []
    family_ids: set[str] = set()
    family_by_name: dict[str, str] = {}
    family_dimensions: dict[str, str] = {}
    for i, fam in enumerate(families):
        where = f"families[{i}]"
        if not isinstance(fam, dict):
            fail(errors, f"{where}: must be an object")
            continue
        fid = fam.get("id")
        if not isinstance(fid, str) or not ID_RE.match(fid):
            fail(errors, f"{where}: id must be kebab-case")
            continue
        if fid in family_ids:
            fail(errors, f"{where}: duplicate family id {fid!r}")
        family_ids.add(fid)
        if not nonempty(fam.get("name")):
            fail(errors, f"{where}: name must be a non-empty string")
        else:
            if fam["name"] in family_by_name:
                fail(errors, f"{where}: duplicate family name {fam['name']!r}")
            family_by_name[fam["name"]] = fid
        if not nonempty(fam.get("essence")):
            fail(errors, f"{where}: essence must be a non-empty string")
        if fam.get("color") not in COLORS:
            fail(errors, f"{where}: unknown accent token {fam.get('color')!r}")
        if fam.get("dimension") not in DIMENSION_IDS:
            fail(errors, f"{where}: unknown dimension {fam.get('dimension')!r}")
        else:
            family_dimensions[fid] = fam["dimension"]
        if not isinstance(fam.get("count"), int) or fam["count"] < 1:
            fail(errors, f"{where}: count must be a positive integer")

    dimensions = data.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        fail(errors, "dimensions must be a non-empty list")
        dimensions = []
    dimension_ids: set[str] = set()
    for i, dim in enumerate(dimensions):
        where = f"dimensions[{i}]"
        if not isinstance(dim, dict):
            fail(errors, f"{where}: must be an object")
            continue
        did = dim.get("id")
        if not isinstance(did, str) or not ID_RE.match(did):
            fail(errors, f"{where}: id must be kebab-case")
            continue
        if did in dimension_ids:
            fail(errors, f"{where}: duplicate dimension id {did!r}")
        dimension_ids.add(did)
        if not nonempty(dim.get("name")):
            fail(errors, f"{where}: name must be a non-empty string")
    missing_dimensions = DIMENSION_IDS - dimension_ids
    if missing_dimensions:
        fail(errors, f"dimensions missing: {sorted(missing_dimensions)}")

    roots = data.get("roots")
    if not isinstance(roots, list) or len(roots) != 1:
        fail(errors, "roots must be a single-item list")
        roots = []
    if errors and not roots:
        print("\n".join("[shape-atlas] " + e for e in errors), file=sys.stderr)
        return 1

    root = roots[0] if roots else {}
    if not isinstance(root, dict):
        fail(errors, "roots[0] must be an object")
        root = {}

    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    sibling_labels: dict[str, set[str]] = {}
    node_count = 0
    note_links = 0
    max_depth = 0
    family_counts: Counter[str] = Counter()
    nodes: list[dict] = []

    def visit(node: dict, parent: dict | None, depth: int) -> None:
        nonlocal node_count, note_links, max_depth
        if not isinstance(node, dict):
            fail(errors, "tree node must be an object")
            return
        nodes.append(node)
        node_count += 1
        max_depth = max(max_depth, depth)
        label = node.get("label")
        nid = node.get("id")
        path = node.get("path")
        where = f"node {nid or path or '<unnamed>'}"

        if not nonempty(label):
            fail(errors, f"{where}: label must be a non-empty string")
        if not isinstance(nid, str) or not ID_RE.match(nid):
            fail(errors, f"{where}: id must be kebab-case")
        elif nid in seen_ids:
            fail(errors, f"{where}: duplicate id")
        else:
            seen_ids.add(nid)
        if not nonempty(path):
            fail(errors, f"{where}: path must be a non-empty string")
        elif path in seen_paths:
            fail(errors, f"{where}: duplicate path {path!r}")
        else:
            seen_paths.add(path)

        kind = node.get("kind")
        if kind not in KINDS:
            fail(errors, f"{where}: kind must be one of {sorted(KINDS)}")
        if depth == 1 and kind != "root":
            fail(errors, f"{where}: the single root must have kind 'root'")
        if depth > 1 and kind == "root":
            fail(errors, f"{where}: only the root may have kind 'root'")

        fid = node.get("family")
        if depth == 1:
            if fid != "geometric-shape":
                fail(errors, f"{where}: root family must be 'geometric-shape'")
        else:
            if fid not in family_ids:
                fail(errors, f"{where}: unknown family {fid!r}")
            else:
                family_counts[fid] += 1
            if depth == 2:
                if kind != "family":
                    fail(errors, f"{where}: top-level branches must have kind 'family'")
                if fid != family_by_name.get(label):
                    fail(errors, f"{where}: top-level family node must name its own family")
            elif parent is not None and fid != parent.get("family"):
                fail(errors, f"{where}: family must match its parent")

        dimension = node.get("dimension")
        if dimension not in dimension_ids:
            fail(errors, f"{where}: unknown dimension {dimension!r}")
        if fid in family_dimensions and dimension != family_dimensions[fid]:
            fail(errors, f"{where}: dimension must match its family")

        if depth == 1:
            expected_path = label
        elif nonempty(parent.get("path") if parent else None) and nonempty(label):
            expected_path = parent["path"] + " → " + label
            if path != expected_path:
                fail(errors, f"{where}: path should be {expected_path!r}")
        if depth > 2 and kind == "family":
            fail(errors, f"{where}: only top-level branches may have kind 'family'")
        if depth > 2 and parent is not None and parent.get("family") == "shape-properties":
            if kind != "property":
                fail(errors, f"{where}: shape-properties children must have kind 'property'")

        if not nonempty(node.get("description")):
            fail(errors, f"{where}: description must be a non-empty string")

        figure = node.get("figure")
        if not isinstance(figure, dict):
            fail(errors, f"{where}: figure must be an object")
        else:
            fkind = figure.get("kind")
            if fkind not in FIGURE_KINDS:
                fail(errors, f"{where}: unknown figure kind {fkind!r}")
            for key in ("variant",):
                if key in figure and not nonempty(figure[key]):
                    fail(errors, f"{where}: figure.{key} must be a non-empty string")
            for key in ("sides", "step"):
                if key in figure and (not isinstance(figure[key], int) or figure[key] < 1):
                    fail(errors, f"{where}: figure.{key} must be a positive integer")

        if "note" in node:
            note = node.get("note")
            if not nonempty(note):
                fail(errors, f"{where}: note must be a non-empty string")
            else:
                rel = Path(note)
                if rel.is_absolute() or ".." in rel.parts:
                    fail(errors, f"{where}: note must be relative to src/corpus/notes")
                elif rel.suffix not in (".md", ".html"):
                    fail(errors, f"{where}: note must end in .md or .html")
                elif not (NOTES / rel).is_file():
                    fail(errors, f"{where}: note does not exist: {note}")
                else:
                    note_links += 1

        children = node.get("children")
        if not isinstance(children, list):
            fail(errors, f"{where}: children must be a list")
            return
        parent_key = nid if isinstance(nid, str) else path
        labels = sibling_labels.setdefault(parent_key, set())
        for child in children:
            if isinstance(child, dict) and nonempty(child.get("label")):
                if child["label"] in labels:
                    fail(errors, f"{where}: duplicate sibling label {child['label']!r}")
                labels.add(child["label"])
            visit(child, node, depth + 1)

    visit(root, None, 1)

    if not isinstance(root, dict) or root.get("kind") != "root":
        fail(errors, "roots[0] must be the root node")
    if root.get("family") != "geometric-shape":
        fail(errors, "root family must be 'geometric-shape'")

    stats = data.get("stats")
    if not isinstance(stats, dict):
        fail(errors, "stats must be an object")
        stats = {}
    expected_stats = {
        "nodes": node_count,
        "families": len(family_ids),
        "maxDepth": max_depth,
        "figures": node_count,
    }
    for key, expected in expected_stats.items():
        if stats.get(key) != expected:
            fail(errors, f"stats.{key} is {stats.get(key)!r}, expected {expected}")
    if not isinstance(stats.get("rows"), int) or stats["rows"] < node_count - 1:
        fail(errors, "stats.rows must be an integer at least the non-root node count")

    for fam in families:
        if not isinstance(fam, dict):
            continue
        fid = fam.get("id")
        if fid in family_counts and fam.get("count") != family_counts[fid]:
            fail(errors, f"families[{fid}].count is {fam.get('count')!r}, "
                         f"expected {family_counts[fid]}")
    top_family_ids = {child.get("family") for child in root.get("children", [])
                      if isinstance(child, dict)}
    if family_ids != top_family_ids:
        fail(errors, "families must match the root's top-level branches")

    if errors:
        print("\n".join("[shape-atlas] " + e for e in errors), file=sys.stderr)
        print(f"[shape-atlas] {len(errors)} error(s)", file=sys.stderr)
        return 1

    kinds = Counter(node.get("kind") for node in nodes)
    print(
        "[shape-atlas] ok: "
        f"{node_count} nodes ({kinds.get('shape', 0)} shapes, "
        f"{kinds.get('family', 0)} families, {kinds.get('property', 0)} properties), "
        f"{len(families)} families, depth {max_depth}, "
        f"{node_count} figures, {note_links} note links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
