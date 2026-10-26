#!/usr/bin/env python3
"""
Terminology-crimes store validator.

Validates src/note/app/data/epistemica/crimes/terminology.json: required
fields, unique kebab ids, enum domains/crimes/severities, resolving related
ids, existing note links, and well-formed sources. Stdlib only.

Usage: python3 src/note/bin/terminology_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
DATA = REPO / "src" / "note" / "app" / "data"
STORE = DATA / "epistemica" / "crimes" / "terminology.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_TEXT = ("term", "crime", "severity", "damage", "sounds_like",
                 "actually_means", "trap", "use_instead")


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
    for key in ("title", "abbr", "version", "intro", "domains", "severities",
                "crime_types", "crimes"):
        if key not in d:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return fail(errors)

    domains = d["domains"]
    severities = d["severities"]
    crime_types = d["crime_types"]
    if not isinstance(domains, list) or not domains:
        errors.append("domains must be a non-empty list")
    if not isinstance(severities, list) or not severities:
        errors.append("severities must be a non-empty list")
    if set(severities) != {"high", "medium", "low"}:
        errors.append("severities must be exactly high/medium/low")
    if not isinstance(crime_types, dict) or not crime_types:
        errors.append("crime_types must be a non-empty object")

    crimes = d["crimes"]
    if not isinstance(crimes, list) or not crimes:
        return fail(errors + ["crimes must be a non-empty list"])

    ids = {}
    for i, c in enumerate(crimes):
        where = f"crimes[{i}]"
        if not isinstance(c, dict):
            errors.append(f"{where} is not an object")
            continue
        cid = c.get("id")
        if not isinstance(cid, str) or not ID_RE.match(cid):
            errors.append(f"{where}: invalid id {cid!r}")
            continue
        if cid in ids:
            errors.append(f"duplicate id: {cid}")
        ids[cid] = c
        for field in REQUIRED_TEXT:
            value = c.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{cid}: missing/empty {field}")
        doms = c.get("domains")
        if not isinstance(doms, list) or not doms:
            errors.append(f"{cid}: domains must be a non-empty list")
        else:
            for dom in doms:
                if dom not in domains:
                    errors.append(f"{cid}: unknown domain {dom!r}")
        if c.get("crime") not in crime_types:
            errors.append(f"{cid}: unknown crime {c.get('crime')!r}")
        if c.get("severity") not in severities:
            errors.append(f"{cid}: unknown severity {c.get('severity')!r}")
        for rel in c.get("related") or []:
            if rel not in ids and rel not in {x.get("id") for x in crimes}:
                errors.append(f"{cid}: related id not found: {rel}")
        for note in c.get("notes") or []:
            if not (DATA / note).is_file():
                errors.append(f"{cid}: note not found: {note}")
        sources = c.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{cid}: sources must be a non-empty list")
        else:
            for src in sources:
                if not isinstance(src, dict) or not src.get("label"):
                    errors.append(f"{cid}: source needs a label")
                    continue
                url = src.get("url")
                if url is not None and not re.match(r"^https?://", url):
                    errors.append(f"{cid}: source url must be http(s): {url!r}")

    if errors:
        return fail(errors)

    by_sev = {}
    for c in crimes:
        by_sev[c["severity"]] = by_sev.get(c["severity"], 0) + 1
    print(f"[terminology] ok: {len(crimes)} terms, "
          f"{len(crime_types)} crime types, {len(domains)} domains, "
          f"{by_sev.get('high', 0)} high-severity -> "
          f"{STORE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
