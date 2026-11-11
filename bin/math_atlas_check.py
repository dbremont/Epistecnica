#!/usr/bin/env python3
"""
Mathematical Area Atlas store validator.

Validates src/corpus/notes/epistemica/mathematical/atlas.json: required
top-level keys, unique kebab-case ids, known families and axes, method
entries with null axes, complete text fields, resolving related ids, and
existing corpus note links. Stdlib only.

Usage: python3 bin/math_atlas_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "src" / "corpus" / "notes"
STORE = NOTES / "epistemica" / "mathematical" / "atlas.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TOP_KEYS = ("title", "version", "subtitle", "intro", "families", "axes", "areas")
COLORS = {
    "--accent-gold", "--accent-cyan", "--accent-violet", "--accent-copper",
    "--accent-copper-light", "--accent-sage", "--accent-plum", "--accent-rose",
    "--accent-amber", "--accent-steel",
}
KINDS = {"area", "method"}
TEXT_FIELDS = ("name", "symbol", "family", "essence", "description")
LIST_FIELDS = ("objects", "operations", "subareas")


def fail(errors, msg):
    errors.append(msg)


def main():
    errors = []
    if not STORE.is_file():
        print(f"[math-atlas] missing store: {STORE}", file=sys.stderr)
        return 1

    try:
        data = json.loads(STORE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[math-atlas] invalid JSON: {exc}", file=sys.stderr)
        return 1

    if not isinstance(data, dict):
        print("[math-atlas] store must be a JSON object", file=sys.stderr)
        return 1

    for key in TOP_KEYS:
        if key not in data:
            fail(errors, f"missing top-level key {key!r}")
    if errors:
        print("\n".join("[math-atlas] " + e for e in errors), file=sys.stderr)
        return 1

    if not isinstance(data["title"], str) or not data["title"].strip():
        fail(errors, "title must be a non-empty string")
    if not isinstance(data["version"], str) or not DATE_RE.match(data["version"]):
        fail(errors, "version must be YYYY-MM-DD")
    for key in ("subtitle", "intro"):
        if not isinstance(data[key], str) or not data[key].strip():
            fail(errors, f"{key} must be a non-empty string")

    families = data["families"]
    if not isinstance(families, list) or not families:
        fail(errors, "families must be a non-empty list")
        families = []
    family_ids = set()
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
        for key in ("name", "essence"):
            if not isinstance(fam.get(key), str) or not fam[key].strip():
                fail(errors, f"{where}: {key} must be a non-empty string")
        if fam.get("color") not in COLORS:
            fail(errors, f"{where}: unknown accent token {fam.get('color')!r}")

    axes = data["axes"]
    if not isinstance(axes, dict):
        fail(errors, "axes must be an object")
        axes = {}
    axis_ids = {}
    for axis in ("properties", "operations"):
        items = axes.get(axis)
        if not isinstance(items, list) or not items:
            fail(errors, f"axes.{axis} must be a non-empty list")
            continue
        ids = set()
        for i, item in enumerate(items):
            where = f"axes.{axis}[{i}]"
            if not isinstance(item, dict):
                fail(errors, f"{where}: must be an object")
                continue
            iid = item.get("id")
            if not isinstance(iid, str) or not ID_RE.match(iid):
                fail(errors, f"{where}: id must be kebab-case")
                continue
            if iid in ids:
                fail(errors, f"{where}: duplicate id {iid!r}")
            ids.add(iid)
            if not isinstance(item.get("name"), str) or not item["name"].strip():
                fail(errors, f"{where}: name must be a non-empty string")
        axis_ids[axis] = ids

    areas = data["areas"]
    if not isinstance(areas, list) or not areas:
        fail(errors, "areas must be a non-empty list")
        areas = []
    area_ids = set()
    note_links = 0
    for i, area in enumerate(areas):
        where = f"areas[{i}]"
        if not isinstance(area, dict):
            fail(errors, f"{where}: must be an object")
            continue
        aid = area.get("id")
        if not isinstance(aid, str) or not ID_RE.match(aid):
            fail(errors, f"{where}: id must be kebab-case")
            continue
        if aid in area_ids:
            fail(errors, f"{where}: duplicate area id {aid!r}")
        area_ids.add(aid)

        for key in TEXT_FIELDS:
            if not isinstance(area.get(key), str) or not area[key].strip():
                fail(errors, f"{where} ({aid}): {key} must be a non-empty string")
        kind = area.get("kind")
        if kind not in KINDS:
            fail(errors, f"{where} ({aid}): kind must be one of {sorted(KINDS)}")
        if area.get("family") not in family_ids:
            fail(errors, f"{where} ({aid}): unknown family {area.get('family')!r}")
        if not isinstance(area.get("stub"), bool):
            fail(errors, f"{where} ({aid}): stub must be a boolean")

        prop, op = area.get("property"), area.get("operation")
        if kind == "method":
            if prop is not None or op is not None:
                fail(errors, f"{where} ({aid}): method entries must have null property/operation")
        else:
            if prop not in axis_ids.get("properties", set()):
                fail(errors, f"{where} ({aid}): unknown property {prop!r}")
            if op not in axis_ids.get("operations", set()):
                fail(errors, f"{where} ({aid}): unknown operation {op!r}")

        for key in LIST_FIELDS:
            val = area.get(key)
            if not isinstance(val, list) or not all(isinstance(x, str) and x.strip() for x in val):
                fail(errors, f"{where} ({aid}): {key} must be a list of non-empty strings")

        notes = area.get("notes")
        if not isinstance(notes, list):
            fail(errors, f"{where} ({aid}): notes must be a list")
            notes = []
        if not area.get("stub") and not notes:
            fail(errors, f"{where} ({aid}): non-stub area must link at least one corpus note")
        seen_paths = set()
        for j, note in enumerate(notes):
            nwhere = f"{where} ({aid}) notes[{j}]"
            if not isinstance(note, dict):
                fail(errors, f"{nwhere}: must be an object")
                continue
            label, path = note.get("label"), note.get("path")
            if not isinstance(label, str) or not label.strip():
                fail(errors, f"{nwhere}: label must be a non-empty string")
            if not isinstance(path, str) or not path.strip():
                fail(errors, f"{nwhere}: path must be a non-empty string")
                continue
            rel = Path(path)
            if rel.is_absolute() or ".." in rel.parts:
                fail(errors, f"{nwhere}: path must be relative to src/corpus/notes")
                continue
            if rel.suffix not in (".md", ".html"):
                fail(errors, f"{nwhere}: path must end in .md or .html")
            if path in seen_paths:
                fail(errors, f"{nwhere}: duplicate note path {path!r}")
            seen_paths.add(path)
            if not (NOTES / rel).is_file():
                fail(errors, f"{nwhere}: note does not exist: {path}")
            else:
                note_links += 1

        related = area.get("related")
        if not isinstance(related, list) or not all(isinstance(x, str) for x in related):
            fail(errors, f"{where} ({aid}): related must be a list of ids")
            related = []
        for rid in related:
            if rid == aid:
                fail(errors, f"{where} ({aid}): related must not include itself")

    # Second pass for forward related references.
    for i, area in enumerate(areas):
        if not isinstance(area, dict):
            continue
        aid = area.get("id")
        for rid in area.get("related", []) if isinstance(area.get("related"), list) else []:
            if isinstance(rid, str) and rid != aid and rid not in area_ids:
                fail(errors, f"areas[{i}] ({aid}): unknown related id {rid!r}")

    if not family_ids:
        fail(errors, "no families defined")
    if not area_ids:
        fail(errors, "no areas defined")

    if errors:
        print("\n".join("[math-atlas] " + e for e in errors), file=sys.stderr)
        print(f"[math-atlas] {len(errors)} error(s)", file=sys.stderr)
        return 1

    kinds = {k: sum(1 for a in areas if a.get("kind") == k) for k in KINDS}
    stubs = sum(1 for a in areas if a.get("stub"))
    print(
        "[math-atlas] ok: "
        f"{kinds['area']} areas, {kinds['method']} methods, {stubs} stubs, "
        f"{len(families)} families, {note_links} note links"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
