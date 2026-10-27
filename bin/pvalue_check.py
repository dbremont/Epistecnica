#!/usr/bin/env python3
"""
P-value atlas store validator.

Validates src/note/app/data/epistemica/validation/atlas/pvalue.json: required
top-level keys, unique kebab-case distribution ids, known families and
engines, complete tail formulas (density/mass, CDF, left, right, two-sided,
free of `$`), parameter specs, resolving related ids and note links, and
well-formed sources. Stdlib only.

Usage: python3 bin/pvalue_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "src" / "note" / "app" / "data"
STORE = DATA / "epistemica" / "validation" / "atlas" / "pvalue.json"

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PARAM_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

TOP_KEYS = ("title", "abbr", "version", "intro", "source", "families",
            "distributions")
TEXT_FIELDS = ("name", "symbol", "family", "support", "parameters",
               "statistic", "definition", "p_convention")
FORMULA_KEYS = ("density", "cdf", "p_left", "p_right", "p_two")
ENGINES = {
    "normal", "student-t", "chi-square", "f", "gamma", "exponential", "beta",
    "uniform", "cauchy", "ks", "binomial", "poisson", "hypergeometric",
    "negative-binomial", "geometric", "multinomial", "permutation",
    "bootstrap", "mann-whitney",
}
RESAMPLING = {"permutation", "bootstrap", "mann-whitney"}


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
    for key in TOP_KEYS:
        if key not in d:
            errors.append(f"missing top-level key: {key}")
    if errors:
        return fail(errors)

    if not DATE_RE.match(str(d["version"])):
        errors.append(f"version must be YYYY-MM-DD: {d['version']!r}")

    families = d["families"]
    if not isinstance(families, dict) or not families:
        return fail(errors + ["families must be a non-empty object"])
    for name, blurb in families.items():
        if not ID_RE.match(name):
            errors.append(f"family name not kebab-case: {name!r}")
        if not isinstance(blurb, str) or not blurb.strip():
            errors.append(f"family {name!r}: missing/empty description")

    distributions = d["distributions"]
    if not isinstance(distributions, list) or not distributions:
        return fail(errors + ["distributions must be a non-empty list"])

    ids = {}
    used_families = set()
    notes_linked = set()
    analytic_count = 0
    for i, item in enumerate(distributions):
        where = f"distributions[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{where} is not an object")
            continue
        did = item.get("id")
        if not isinstance(did, str) or not ID_RE.match(did):
            errors.append(f"{where}: invalid id {did!r}")
            continue
        if did in ids:
            errors.append(f"duplicate id: {did}")
        ids[did] = item

        for field in TEXT_FIELDS:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{did}: missing/empty {field}")
        if item.get("family") not in families:
            errors.append(f"{did}: unknown family {item.get('family')!r}")
        else:
            used_families.add(item["family"])

        engine = item.get("engine")
        if engine not in ENGINES:
            errors.append(f"{did}: unknown engine {engine!r}")
        analytic = item.get("analytic")
        if not isinstance(analytic, bool):
            errors.append(f"{did}: analytic must be true/false")
        elif engine in RESAMPLING and analytic:
            errors.append(f"{did}: resampling engine {engine!r} cannot be analytic")
        elif engine not in RESAMPLING and not analytic:
            errors.append(f"{did}: engine {engine!r} should be analytic")
        if analytic:
            analytic_count += 1

        formulas = item.get("formulas")
        if not isinstance(formulas, dict):
            errors.append(f"{did}: formulas must be an object")
        else:
            for key in FORMULA_KEYS:
                tex = formulas.get(key)
                if not isinstance(tex, str) or not tex.strip():
                    errors.append(f"{did}: missing/empty formula {key}")
                elif "$" in tex:
                    errors.append(f"{did}: formula {key} must not contain '$'")

        params = item.get("params")
        if not isinstance(params, list) or not params:
            errors.append(f"{did}: params must be a non-empty list")
        else:
            seen = set()
            for p in params:
                if not isinstance(p, dict):
                    errors.append(f"{did}: params entry is not an object")
                    continue
                pname = p.get("name")
                if not isinstance(pname, str) or not PARAM_RE.match(pname):
                    errors.append(f"{did}: invalid param name {pname!r}")
                    continue
                if pname in seen:
                    errors.append(f"{did}: duplicate param {pname!r}")
                seen.add(pname)
                for need in ("label", "default", "min", "max"):
                    if need not in p:
                        errors.append(f"{did}.{pname}: missing {need}")
                lo, hi, default = p.get("min"), p.get("max"), p.get("default")
                if all(isinstance(x, (int, float)) for x in (lo, hi, default)):
                    if not lo < hi:
                        errors.append(f"{did}.{pname}: min must be < max")
                    if not lo <= default <= hi:
                        errors.append(f"{did}.{pname}: default outside [min, max]")

        tests = item.get("tests")
        if not isinstance(tests, list) or not tests or any(
            not isinstance(t, str) or not t.strip() for t in tests
        ):
            errors.append(f"{did}: tests must be a non-empty list of strings")

        for rel in item.get("related") or []:
            if rel not in {x.get("id") for x in distributions}:
                errors.append(f"{did}: related id not found: {rel}")

        for note in item.get("notes") or []:
            if not (DATA / note).is_file():
                errors.append(f"{did}: note not found: {note}")
            else:
                notes_linked.add(note)

        sources = item.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{did}: sources must be a non-empty list")
        else:
            for src in sources:
                if not isinstance(src, dict) or not src.get("label"):
                    errors.append(f"{did}: source needs a label")
                    continue
                url = src.get("url")
                if url is not None and not re.match(r"^https?://", url):
                    errors.append(f"{did}: source url must be http(s): {url!r}")

    for family in families:
        if family not in used_families:
            errors.append(f"family {family!r} has no distributions")

    if errors:
        return fail(errors)

    print(f"[pvalue] ok: {len(distributions)} distributions, "
          f"{len(families)} families ({analytic_count} analytic, "
          f"{len(distributions) - analytic_count} resampling), "
          f"{len(notes_linked)} linked notes -> {STORE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
