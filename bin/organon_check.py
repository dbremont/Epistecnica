#!/usr/bin/env python3
"""Validate the Organon observation-domain catalogue.

Checks src/corpus/notes/epistemica/observation/organon.json against the rules
stated in organon.md: one kind per entry, the type decides the allowed extra
fields, family/purpose/part_of references resolve, note paths exist.

Part of `make check` (make organon-check).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STORE = REPO / "src" / "corpus" / "notes" / "epistemica" / "observation" / "organon.json"
CORPUS = REPO / "src" / "corpus"

BASE = ("id", "name", "type", "description", "note")
ALLOWED = {
    "activity": set(),
    "design": set(),
    "method": {"lane"},
    "technique": {"family", "purpose", "principle", "observable", "limit", "year"},
    "instrument": {"part_of"},
    "sensor": {"part_of"},
    "standard": set(),
    "record": set(),
    "theory": set(),
}
REQUIRED = {
    "technique": {"family", "purpose", "principle", "observable", "limit"},
    "instrument": {"part_of"},
}


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def main() -> int:
    if not STORE.exists():
        print(f"[organon] missing {STORE}", file=sys.stderr)
        return 1
    data = json.loads(STORE.read_text())
    errors: list[str] = []

    types = set(data.get("types") or [])
    purposes = set(data.get("purposes") or [])
    families = data.get("families") or []
    entries = data.get("entries") or []
    family_ids = {f.get("id") for f in families}

    if not types or not entries:
        fail(errors, "store needs a non-empty `types` and `entries`")
    for t in ("technique", "family"):
        if t == "family":
            continue
        if t not in types:
            fail(errors, f"type vocabulary is missing `{t}`")

    seen: dict[str, dict] = {}
    for i, e in enumerate(entries):
        where = f"entries[{i}] ({e.get('id', '?')})"
        if not isinstance(e, dict):
            fail(errors, f"{where}: not an object")
            continue
        eid = e.get("id")
        if not eid or not isinstance(eid, str):
            fail(errors, f"{where}: missing id")
            continue
        if eid in seen:
            fail(errors, f"{where}: duplicate id")
        seen[eid] = e
        for field in ("name", "type", "description"):
            if not e.get(field):
                fail(errors, f"{where}: missing `{field}`")
        etype = e.get("type")
        if etype not in types:
            fail(errors, f"{where}: unknown type `{etype}`")
            continue
        extra = set(e) - set(BASE)
        illegal = extra - ALLOWED.get(etype, set())
        if illegal:
            fail(errors, f"{where}: type `{etype}` does not allow {sorted(illegal)}")
        missing = REQUIRED.get(etype, set()) - set(e)
        if missing:
            fail(errors, f"{where}: type `{etype}` requires {sorted(missing)}")
        if e.get("family") and e["family"] not in family_ids:
            fail(errors, f"{where}: family `{e['family']}` not declared")
        if e.get("purpose") and e["purpose"] not in purposes:
            fail(errors, f"{where}: purpose `{e['purpose']}` not declared")
        note = e.get("note")
        if note:
            if not str(note).startswith("notes/"):
                fail(errors, f"{where}: note must start with `notes/`")
            elif not (CORPUS / note).exists():
                fail(errors, f"{where}: note path does not exist: {note}")

    for eid, e in seen.items():
        if e.get("type") not in ("instrument", "sensor"):
            continue
        parent = e.get("part_of")
        if parent and (parent not in seen or seen[parent].get("type") != "technique"):
            fail(errors, f"entries ({eid}): part_of `{parent}` is not a technique")

    used = {e.get("family") for e in entries if e.get("type") == "technique"}
    for fid in family_ids:
        if fid not in used:
            fail(errors, f"family `{fid}` is declared but no technique uses it")
    for f in families:
        for field in ("id", "name", "principle", "observable", "limit"):
            if not f.get(field):
                fail(errors, f"family `{f.get('id', '?')}`: missing `{field}`")

    counts: dict[str, int] = {}
    for e in entries:
        counts[e.get("type", "?")] = counts.get(e.get("type", "?"), 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))

    if errors:
        print(f"[organon] {len(errors)} problem(s)", file=sys.stderr)
        for msg in errors:
            print(f"  ! {msg}", file=sys.stderr)
        return 1
    print(f"[organon] ok: {len(entries)} entries ({summary}), {len(families)} families, {len(purposes)} purposes -> {STORE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
