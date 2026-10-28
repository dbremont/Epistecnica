#!/usr/bin/env python3
"""
Goodness-of-fit atlas store validator.

Validates src/note/app/data/epistemica/validation/atlas/gof.json: required
top-level keys, unique kebab-case law and measure ids, known law engines and
measure kinds, complete LaTeX formulas (free of `$`), parameter specs in
range, an estimation count consistent with the parameters, and a selftest
block whose cases reference existing laws/measures with the right sample and
expected values. Stdlib only.

Usage: python3 bin/gof_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "src" / "note" / "app" / "data"
STORE = DATA / "epistemica" / "validation" / "atlas" / "gof.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PARAM_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TOP_KEYS = ("title", "abbr", "version", "intro", "source", "kinds",
            "measures", "laws", "selftest")
LAW_TEXT = ("name", "symbol", "support", "density", "cdf", "sampler",
            "estimator", "notes")
MEASURE_TEXT = ("name", "symbol", "definition", "statistic", "df", "notes")
ENGINES = {
    "normal", "exponential", "gamma", "weibull", "lognormal", "uniform",
    "beta", "poisson", "binomial",
}
MEASURE_KINDS = {"binned", "edf"}
NULLS = {"chi-square", "kolmogorov", "anderson-darling", "bootstrap"}
LAW_KINDS = {"continuous", "discrete"}
SELFTEST_KINDS = {"statistic", "fit"}


def fail(errors: list) -> int:
    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    return 1


def is_num(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def check_tex(errors: list, where: str, field: str, tex) -> None:
    if not isinstance(tex, str) or not tex.strip():
        errors.append(f"{where}: missing/empty {field}")
    elif "$" in tex:
        errors.append(f"{where}: {field} must not contain '$'")


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
    for key in TOP_KEYS:
        if key not in d:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return fail(errors)

    if not DATE_RE.match(str(d["version"])):
        errors.append(f"version must be YYYY-MM-DD: {d['version']!r}")

    kinds = d["kinds"]
    if not isinstance(kinds, dict) or not kinds:
        return fail(errors + ["kinds must be a non-empty object"])
    for name, blurb in kinds.items():
        if name not in LAW_KINDS:
            errors.append(f"unknown kind: {name!r}")
        if not isinstance(blurb, str) or not blurb.strip():
            errors.append(f"kind {name!r}: missing/empty description")

    measures = d["measures"]
    if not isinstance(measures, list) or not measures:
        return fail(errors + ["measures must be a non-empty list"])
    measure_by_id = {}
    for i, item in enumerate(measures):
        where = f"measures[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{where} is not an object")
            continue
        mid = item.get("id")
        if not isinstance(mid, str) or not ID_RE.match(mid):
            errors.append(f"{where}: invalid id {mid!r}")
            continue
        if mid in measure_by_id:
            errors.append(f"duplicate measure id: {mid}")
        measure_by_id[mid] = item
        for field in MEASURE_TEXT:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{mid}: missing/empty {field}")
        if item.get("kind") not in MEASURE_KINDS:
            errors.append(f"{mid}: unknown measure kind {item.get('kind')!r}")
        if item.get("null") not in NULLS:
            errors.append(f"{mid}: unknown null {item.get('null')!r}")
        check_tex(errors, mid, "formula", item.get("formula"))

    laws = d["laws"]
    if not isinstance(laws, list) or not laws:
        return fail(errors + ["laws must be a non-empty list"])
    law_by_id = {}
    used_kinds = set()
    for i, item in enumerate(laws):
        where = f"laws[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{where} is not an object")
            continue
        lid = item.get("id")
        if not isinstance(lid, str) or not ID_RE.match(lid):
            errors.append(f"{where}: invalid id {lid!r}")
            continue
        if lid in law_by_id:
            errors.append(f"duplicate law id: {lid}")
        law_by_id[lid] = item

        for field in LAW_TEXT:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{lid}: missing/empty {field}")
        if item.get("kind") not in kinds:
            errors.append(f"{lid}: kind not declared in kinds: {item.get('kind')!r}")
        else:
            used_kinds.add(item["kind"])
        if item.get("engine") not in ENGINES:
            errors.append(f"{lid}: unknown engine {item.get('engine')!r}")

        params = item.get("params")
        if not isinstance(params, list) or not params:
            errors.append(f"{lid}: params must be a non-empty list")
            params = []
        seen = set()
        for p in params:
            if not isinstance(p, dict):
                errors.append(f"{lid}: params entry is not an object")
                continue
            pname = p.get("name")
            if not isinstance(pname, str) or not PARAM_RE.match(pname):
                errors.append(f"{lid}: invalid param name {pname!r}")
                continue
            if pname in seen:
                errors.append(f"{lid}: duplicate param {pname!r}")
            seen.add(pname)
            for need in ("label", "default", "min", "max", "step"):
                if need not in p:
                    errors.append(f"{lid}.{pname}: missing {need}")
            lo, hi, default = p.get("min"), p.get("max"), p.get("default")
            if all(is_num(x) for x in (lo, hi, default)):
                if not lo < hi:
                    errors.append(f"{lid}.{pname}: min must be < max")
                if not lo <= default <= hi:
                    errors.append(f"{lid}.{pname}: default outside [min, max]")
            if p.get("integer") not in (None, True, False):
                errors.append(f"{lid}.{pname}: integer must be true/false")

        m = item.get("m")
        if not isinstance(m, int) or isinstance(m, bool) or m < 1:
            errors.append(f"{lid}: m must be a positive integer (estimated parameters)")
        elif m > len(params):
            errors.append(f"{lid}: m={m} exceeds the parameter count {len(params)}")

    for kind in kinds:
        if kind not in used_kinds:
            errors.append(f"kind {kind!r} has no laws")

    selftest = d["selftest"]
    if not isinstance(selftest, list) or not selftest:
        return fail(errors + ["selftest must be a non-empty list"])
    seen_ids = set()
    statistic_cases = fit_cases = 0
    for i, case in enumerate(selftest):
        where = f"selftest[{i}]"
        if not isinstance(case, dict):
            errors.append(f"{where} is not an object")
            continue
        cid = case.get("id")
        if not isinstance(cid, str) or not ID_RE.match(cid):
            errors.append(f"{where}: invalid id {cid!r}")
            continue
        if cid in seen_ids:
            errors.append(f"duplicate selftest id: {cid}")
        seen_ids.add(cid)

        law = law_by_id.get(case.get("law"))
        if law is None:
            errors.append(f"{cid}: unknown law {case.get('law')!r}")
        sample = case.get("sample")
        if not isinstance(sample, list) or not sample or not all(is_num(x) for x in sample):
            errors.append(f"{cid}: sample must be a non-empty list of numbers")

        kind = case.get("kind")
        if kind not in SELFTEST_KINDS:
            errors.append(f"{cid}: unknown kind {kind!r}")
            continue

        if kind == "fit":
            fit_cases += 1
            expected = case.get("expected")
            if not isinstance(expected, dict) or not expected:
                errors.append(f"{cid}: fit case needs an expected object")
                continue
            if not all(is_num(v) for v in expected.values()):
                errors.append(f"{cid}: expected values must be numbers")
            if law is not None:
                known = {p.get("name") for p in law.get("params") or []}
                for key in expected:
                    if key not in known:
                        errors.append(f"{cid}: expected parameter {key!r} not in {law.get('id')}")
            continue

        statistic_cases += 1
        measure = measure_by_id.get(case.get("measure"))
        if measure is None:
            errors.append(f"{cid}: unknown measure {case.get('measure')!r}")
        elif law is not None:
            if measure.get("kind") == "edf" and law.get("kind") == "discrete":
                errors.append(f"{cid}: EDF measure on a discrete law")
        params = case.get("params")
        if not isinstance(params, dict) or not params:
            errors.append(f"{cid}: statistic case needs params")
        elif law is not None:
            known = {p.get("name") for p in law.get("params") or []}
            for key in params:
                if key not in known:
                    errors.append(f"{cid}: param {key!r} not in {law.get('id')}")
        if not is_num(case.get("expected")):
            errors.append(f"{cid}: statistic case needs a numeric expected value")
        edges = case.get("edges")
        if edges is not None:
            if not isinstance(edges, list) or not edges or not all(is_num(x) for x in edges):
                errors.append(f"{cid}: edges must be a non-empty list of numbers")
            elif edges != sorted(edges):
                errors.append(f"{cid}: edges must be sorted")

    if errors:
        return fail(errors)

    print(f"[gof] ok: {len(laws)} laws, {len(measure_by_id)} measures, "
          f"{statistic_cases} statistic + {fit_cases} fit selftest cases, "
          f"{len(kinds)} kinds -> {STORE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
