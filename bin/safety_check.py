#!/usr/bin/env python3
"""
Product-safety hazard store validator.

Validates src/corpus/notes/social/good/safety.json: required top-level keys,
kebab-case ids unique across the store, hazard classes that every hazard
resolves to, the three-tier control hierarchy present and ordered, enum
severity and exposure routes, non-empty mechanisms/outcomes/domains/
standards/signals, reference groups numbered from 1 and actually used,
references whose group exists and whose url is https, and the companion
safety.html beside the store that fetches it. Stdlib only.

Usage: python3 bin/safety_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STORE = REPO / "src" / "corpus" / "notes" / "social" / "good" / "safety.json"
PAGE = STORE.with_suffix(".html")

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TOP_KEYS = ("title", "version", "intro", "source", "hierarchy", "hierarchyLabels",
            "classes", "hazards", "referenceGroups", "references")
HIERARCHY = ("inherent", "safeguarding", "information")
SEVERITIES = {"low", "medium", "high"}
EXPOSURES = {"ingestion", "inhalation", "dermal", "contact", "thermal",
             "electrical", "none"}


def fail(errors: list) -> int:
    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    return 1


def text(errors: list, where: str, field: str, value) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where}: missing/empty {field}")


def text_list(errors: list, where: str, field: str, value) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{where}: {field} must be a non-empty list")
        return
    for i, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{where}: {field}[{i}] is empty")


def main() -> int:
    if not STORE.exists():
        return fail([f"missing store: {STORE}"])
    try:
        data = json.loads(STORE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return fail([f"{STORE.name}: invalid JSON — {e}"])

    errors: list = []
    if not isinstance(data, dict):
        return fail(["store must be a JSON object"])

    for key in TOP_KEYS:
        if key not in data:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return fail(errors)

    text(errors, "store", "title", data["title"])
    text(errors, "store", "version", data["version"])
    text(errors, "store", "intro", data["intro"])
    text(errors, "store", "source", data["source"])
    if isinstance(data["source"], str) and not (REPO / "src" / "corpus" / data["source"]).exists():
        errors.append(f"source note does not exist: {data['source']}")

    if data["hierarchy"] != list(HIERARCHY):
        errors.append(f"hierarchy must be {list(HIERARCHY)}")
    labels = data["hierarchyLabels"]
    if not isinstance(labels, dict):
        errors.append("hierarchyLabels must be an object")
    else:
        for key in HIERARCHY:
            text(errors, "hierarchyLabels", key, labels.get(key))

    class_ids = []
    for i, c in enumerate(data["classes"]):
        where = f"classes[{i}]"
        cid = c.get("id")
        if not isinstance(cid, str) or not ID_RE.match(cid):
            errors.append(f"{where}: bad id {cid!r}")
        else:
            class_ids.append(cid)
        text(errors, where, "label", c.get("label"))
        text(errors, where, "desc", c.get("desc"))
    if len(set(class_ids)) != len(class_ids):
        errors.append("class ids are not unique")

    ref_ids = [r.get("id") for r in data["references"]]
    if len(set(ref_ids)) != len(ref_ids):
        errors.append("reference ids are not unique")

    hazard_ids = []
    used_refs = set()
    per_class = {cid: 0 for cid in class_ids}
    per_severity = {s: 0 for s in SEVERITIES}
    for i, h in enumerate(data["hazards"]):
        where = f"hazards[{i}] ({h.get('id', '?')})"
        hid = h.get("id")
        if not isinstance(hid, str) or not ID_RE.match(hid):
            errors.append(f"{where}: bad id {hid!r}")
        else:
            hazard_ids.append(hid)
        if h.get("class") not in per_class:
            errors.append(f"{where}: unknown class {h.get('class')!r}")
        else:
            per_class[h["class"]] += 1
        text(errors, where, "label", h.get("label"))
        text(errors, where, "mechanism", h.get("mechanism"))
        text(errors, where, "outcome", h.get("outcome"))
        sev = h.get("severity")
        if sev not in SEVERITIES:
            errors.append(f"{where}: severity {sev!r} not in {sorted(SEVERITIES)}")
        else:
            per_severity[sev] += 1
        if h.get("exposure") not in EXPOSURES:
            errors.append(f"{where}: exposure {h.get('exposure')!r} not in {sorted(EXPOSURES)}")
        text_list(errors, where, "domains", h.get("domains"))
        text_list(errors, where, "standards", h.get("standards"))
        text_list(errors, where, "signals", h.get("signals"))
        controls = h.get("controls")
        if not isinstance(controls, dict):
            errors.append(f"{where}: controls must be an object")
        else:
            for key in HIERARCHY:
                if not isinstance(controls.get(key), str) or not controls[key].strip():
                    errors.append(f"{where}: controls.{key} missing or empty")
            extra = set(controls) - set(HIERARCHY)
            if extra:
                errors.append(f"{where}: unexpected control tiers {sorted(extra)}")
        refs = h.get("refs", [])
        if not isinstance(refs, list):
            errors.append(f"{where}: refs must be a list")
        else:
            for rid in refs:
                if rid not in ref_ids:
                    errors.append(f"{where}: ref {rid!r} not in references")
                used_refs.add(rid)
    if len(set(hazard_ids)) != len(hazard_ids):
        errors.append("hazard ids are not unique")
    for cid, n in per_class.items():
        if n == 0:
            errors.append(f"class {cid!r} has no hazards")

    groups = data["referenceGroups"]
    group_ids = []
    numbers = []
    for i, g in enumerate(groups):
        where = f"referenceGroups[{i}]"
        gid = g.get("id")
        if not isinstance(gid, str) or not ID_RE.match(gid):
            errors.append(f"{where}: bad id {gid!r}")
        else:
            group_ids.append(gid)
        num = g.get("number")
        if not isinstance(num, int) or isinstance(num, bool) or num < 1:
            errors.append(f"{where}: number must be a positive integer")
        else:
            numbers.append(num)
        text(errors, where, "label", g.get("label"))
    if len(set(group_ids)) != len(group_ids):
        errors.append("reference-group ids are not unique")
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        errors.append(f"reference-group numbers must run 1..n in order, got {numbers}")

    per_group = {gid: 0 for gid in group_ids}
    for i, r in enumerate(data["references"]):
        where = f"references[{i}] ({r.get('id', '?')})"
        rid = r.get("id")
        if not isinstance(rid, str) or not ID_RE.match(rid):
            errors.append(f"{where}: bad id {rid!r}")
        if r.get("group") not in per_group:
            errors.append(f"{where}: unknown group {r.get('group')!r}")
        else:
            per_group[r["group"]] += 1
        text(errors, where, "title", r.get("title"))
        text(errors, where, "desc", r.get("desc"))
        url = r.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{where}: url must be https://")
    for gid, n in per_group.items():
        if n == 0:
            errors.append(f"reference group {gid!r} has no references")
    for rid in ref_ids:
        if rid not in used_refs:
            print(f"  ~ reference {rid!r} is not cited by any hazard")

    if not PAGE.exists():
        errors.append(f"missing companion page: {PAGE.name}")
    else:
        page = PAGE.read_text(encoding="utf-8")
        if "safety.json" not in page:
            errors.append(f"{PAGE.name}: does not reference safety.json")
        if "fetch(" not in page:
            errors.append(f"{PAGE.name}: does not fetch its store")

    if errors:
        return fail(errors)

    print(f"[safety] {data['title']} v{data['version']}")
    print(f"[safety] {len(class_ids)} classes, {len(hazard_ids)} hazards, "
          f"{len(ref_ids)} references in {len(group_ids)} groups")
    print("[safety] severity: " + ", ".join(f"{k}={per_severity[k]}" for k in sorted(SEVERITIES)))
    print("[safety] per class: " + ", ".join(f"{k}={v}" for k, v in per_class.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
