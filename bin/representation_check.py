#!/usr/bin/env python3
"""Validate the social representation stores against their systems catalogues.

Strict for the government store (the one the government view authors):

- every system the profiles name exists in the systems catalogue;
- every characteristic element exists in that system (once — duplicate element
  names make a flat profile object lossy and are an error in the catalogue);
- every assigned value is in the element's value set (``null`` marks an
  element explicitly not applicable);
- the store pins the version of every system it was read under;
- country names resolve against the polity roster (reported, not fatal, so a
  new country can be profiled before its instance exists).

The public-organization store is checked the same way but its drift is
reported as warnings: it predates this checker and its profiles name elements
and values the systems catalogue no longer carries.

Part of ``make check``.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REP = REPO / "src" / "corpus" / "notes" / "social" / "representation"
POLITY = REPO / "src" / "corpus" / "notes" / "social" / "collective" / "polity" / "data.json"

GOV_SYSTEMS = REP / "gov-wide-administration-comparative-system-representation.json"
GOV_PROFILES = REP / "government_representation.json"
ORG_SYSTEMS = REP / "public-organization-characterization-systems.json"
ORG_PROFILES = REP / "public-organization-representation.json"

errors: list[str] = []
warnings: list[str] = []


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def report(strict: bool, message: str) -> None:
    (errors if strict else warnings).append(message)


def system_index(data: dict, strict: bool) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for system in data.get("systems", []):
        name = system.get("name")
        if not name:
            report(strict, "systems catalogue: a system has no name")
            continue
        if name in index:
            report(strict, f"systems catalogue: duplicate system {name!r}")
        index[name] = system
        seen: set[str] = set()
        for element in system.get("characteristic_element_set", []):
            element_name = element.get("name")
            if not element_name:
                report(strict, f"system {name}: an element has no name")
                continue
            if element_name in seen:
                report(
                    strict,
                    f"system {name}: duplicate element {element_name!r} "
                    "(names must be unique across the system's groups)",
                )
            seen.add(element_name)
            if not element.get("value_set"):
                report(strict, f"system {name}: element {element_name!r} has no value set")
    return index


def check_profiles(
    label: str,
    profiles: dict[str, dict],
    systems: dict[str, dict],
    strict: bool,
) -> tuple[int, int]:
    """Check one profile map; return (entries, assignments)."""
    assigned = 0
    for entry_name, entry in profiles.items():
        if not isinstance(entry, dict) or not entry:
            report(strict, f"{label}: {entry_name!r} has no system profile")
            continue
        for system_name, values in entry.items():
            system = systems.get(system_name)
            if not system:
                report(strict, f"{label}: {entry_name!r} names unknown system {system_name!r}")
                continue
            elements = {
                element["name"]: element
                for element in system.get("characteristic_element_set", [])
            }
            if not isinstance(values, dict):
                report(strict, f"{label}: {entry_name!r} / {system_name} is not an object")
                continue
            for element_name, value in values.items():
                element = elements.get(element_name)
                if not element:
                    report(
                        strict,
                        f"{label}: {entry_name!r} / {system_name} names unknown element {element_name!r}",
                    )
                    continue
                if value is None:
                    continue
                if value not in element.get("value_set", []):
                    report(
                        strict,
                        f"{label}: {entry_name!r} / {system_name} / {element_name!r} "
                        f"value {value!r} is not in the value set",
                    )
                else:
                    assigned += 1
    return len(profiles), assigned


def main() -> int:
    gov_systems = system_index(load(GOV_SYSTEMS), strict=True)
    org_systems = system_index(load(ORG_SYSTEMS), strict=False)

    gov = load(GOV_PROFILES)
    meta = gov.get("meta") or {}
    pinned = meta.get("systems") or {}
    expected = {name: system.get("version") for name, system in gov_systems.items()}
    if pinned != expected:
        errors.append(
            "government_representation: meta.systems does not match the systems catalogue "
            f"({pinned} != {expected})"
        )

    countries = gov.get("countries") or {}
    n_countries, n_assignments = check_profiles(
        "government_representation", countries, gov_systems, strict=True
    )

    roster = {
        (code.get("name") or "").strip().lower()
        for code in (load(POLITY).get("codes") or {}).values()
    }
    for name in countries:
        if name.strip().lower() not in roster:
            warnings.append(f"government_representation: {name!r} is not in the polity roster")

    org = load(ORG_PROFILES)
    organizations = {
        org_entry.get("id"): org_entry for org_entry in org.get("organizations", [])
    }
    org_profiles = {
        entry_id: entry.get("profiles") or {}
        for entry_id, entry in organizations.items()
        if entry_id
    }
    n_orgs, n_org_assignments = check_profiles(
        "public-organization-representation", org_profiles, org_systems, strict=False
    )
    for entry in organizations.values():
        confidence = entry.get("confidence")
        if confidence is not None and confidence not in ("high", "medium", "low"):
            warnings.append(
                f"public-organization-representation: {entry.get('id')!r} "
                f"has invalid confidence {confidence!r}"
            )

    for warning in warnings:
        print(f"[representation] warning: {warning}")
    for error in errors:
        print(f"[representation] ERROR: {error}")
    if errors:
        print(f"[representation] {len(errors)} error(s)")
        return 1
    print(
        f"[representation] ok: {n_countries} government(s), {n_assignments} assignment(s); "
        f"{n_orgs} organization(s), {n_org_assignments} assignment(s)"
        + (f"; {len(warnings)} warning(s)" if warnings else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
