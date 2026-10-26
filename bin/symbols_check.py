#!/usr/bin/env python3
"""
Symbol-atlas store validator.

Validates src/note/app/data/epistemica/symbols/symbols.json: required
fields, unique kebab ids, enum categories, non-empty symbol/description/
origins/usage text, resolving related ids, existing note links, and
well-formed sources. Stdlib only.

Usage: python3 bin/symbols_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "src" / "note" / "app" / "data"
STORE = DATA / "epistemica" / "symbols" / "symbols.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_TEXT = ("symbol", "name", "description", "origins", "usage")


def fail(errors: list) -> int:
    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    return 1


def main() -> int:
    if not STORE.is_file():
        print(f"ERROR: store not found: {STORE}", file=sys.stderr)
        return 1
    try:
        d = json.loads(STORE.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors = []
    for key in ("title", "abbr", "version", "intro", "source", "categories",
                "symbols"):
        if key not in d:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return fail(errors)

    categories = d["categories"]
    if not isinstance(categories, dict) or not categories:
        return fail(errors + ["categories must be a non-empty object"])
    for name, blurb in categories.items():
        if not ID_RE.match(name):
            errors.append(f"category name not kebab-case: {name!r}")
        if not isinstance(blurb, str) or not blurb.strip():
            errors.append(f"category {name!r}: missing/empty description")

    symbols = d["symbols"]
    if not isinstance(symbols, list) or not symbols:
        return fail(errors + ["symbols must be a non-empty list"])

    ids = {}
    notes_linked = set()
    for i, s in enumerate(symbols):
        where = f"symbols[{i}]"
        if not isinstance(s, dict):
            errors.append(f"{where} is not an object")
            continue
        sid = s.get("id")
        if not isinstance(sid, str) or not ID_RE.match(sid):
            errors.append(f"{where}: invalid id {sid!r}")
            continue
        if sid in ids:
            errors.append(f"duplicate id: {sid}")
        ids[sid] = s
        for field in REQUIRED_TEXT:
            value = s.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{sid}: missing/empty {field}")
        latex = s.get("latex")
        if latex is not None and (not isinstance(latex, str) or not latex.strip()):
            errors.append(f"{sid}: latex must be a non-empty string")
        cats = s.get("categories")
        if not isinstance(cats, list) or not cats:
            errors.append(f"{sid}: categories must be a non-empty list")
        else:
            for cat in cats:
                if cat not in categories:
                    errors.append(f"{sid}: unknown category {cat!r}")
        aliases = s.get("aliases")
        if aliases is not None and (
            not isinstance(aliases, list)
            or any(not isinstance(a, str) or not a.strip() for a in aliases)
        ):
            errors.append(f"{sid}: aliases must be a list of non-empty strings")
        for rel in s.get("related") or []:
            if rel not in {x.get("id") for x in symbols}:
                errors.append(f"{sid}: related id not found: {rel}")
        for note in s.get("notes") or []:
            if not (DATA / note).is_file():
                errors.append(f"{sid}: note not found: {note}")
            else:
                notes_linked.add(note)
        sources = s.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{sid}: sources must be a non-empty list")
        else:
            for src in sources:
                if not isinstance(src, dict) or not src.get("label"):
                    errors.append(f"{sid}: source needs a label")
                    continue
                url = src.get("url")
                if url is not None and not re.match(r"^https?://", url):
                    errors.append(f"{sid}: source url must be http(s): {url!r}")

    if errors:
        return fail(errors)

    print(f"[symbols] ok: {len(symbols)} symbols, {len(categories)} categories, "
          f"{len(notes_linked)} linked notes -> {STORE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
