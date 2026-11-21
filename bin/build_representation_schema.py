#!/usr/bin/env python3
"""Build the JSON schemas of the social representation stores.

One schema per data file, named ``<data-file>.schema.json`` beside it:

- ``gov-wide-administration-comparative-system-representation.schema.json``
- ``public-organization-characterization-systems.schema.json``
- ``government_representation.schema.json``
- ``public-organization-representation.schema.json``

The two systems catalogues produce their own schemas; the two profile stores
produce schemas whose ``$defs`` are the characterisation schemas of every
system (one property per characteristic element, enumerated with that
element's value set). Regenerate after any edit of a systems catalogue:

    make representation-schema
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REP = REPO / "src" / "corpus" / "notes" / "social" / "representation"

GOV_SYSTEMS = "gov-wide-administration-comparative-system-representation"
ORG_SYSTEMS = "public-organization-characterization-systems"
GOV_PROFILES = "government_representation"
ORG_PROFILES = "public-organization-representation"

SCHEMA_ID = "https://naturgnosis.org/schemas/"
DRAFT = "https://json-schema.org/draft/2020-12/schema"


def load(stem: str) -> dict:
    return json.loads((REP / f"{stem}.json").read_text(encoding="utf-8"))


def write(stem: str, schema: dict) -> None:
    path = REP / f"{stem}.schema.json"
    path.write_text(
        json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[representation-schema] {path.relative_to(REPO)}")


def element_schema(element: dict) -> dict:
    values = list(element.get("value_set") or [])
    schema = {
        "type": ["string", "null"],
        "enum": values + [None],
    }
    if element.get("description"):
        schema["description"] = element["description"]
    return schema


def system_schema(system: dict) -> dict:
    """The characterisation schema of one system: element name -> value set."""
    return {
        "type": "object",
        "description": system.get("description", ""),
        "additionalProperties": False,
        "properties": {
            element["name"]: element_schema(element)
            for element in system.get("characteristic_element_set", [])
        },
    }


def system_catalogue_schema(stem: str, data: dict) -> dict:
    meta = data.get("meta") or {}
    return {
        "$schema": DRAFT,
        "$id": SCHEMA_ID + f"{stem}.schema.json",
        "title": (meta.get("space") or {}).get("name") or stem,
        "description": (
            "A comparative representation systems catalogue: a shared meta block "
            "and the systems, each a set of characteristic elements with their "
            "value sets and assignment rules."
        ),
        "type": "object",
        "required": ["meta", "systems"],
        "properties": {
            "meta": {
                "type": "object",
                "properties": {
                    "space": {"type": "object"},
                    "universe": {"type": "object"},
                    "description": {"type": "string"},
                    "version": {"type": ["string", "integer", "number"]},
                },
            },
            "systems": {
                "type": "array",
                "minItems": 1,
                "items": {"$ref": "#/$defs/system"},
            },
        },
        "additionalProperties": True,
        "$defs": {
            "system": {
                "type": "object",
                "required": [
                    "name",
                    "title",
                    "version",
                    "characteristic_element_set",
                ],
                "properties": {
                    "name": {"type": "string", "pattern": "^[a-z0-9-]+$"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "frame_basis": {"type": "string"},
                    "provenance": {"type": "string"},
                    "universe": {"type": ["string", "object"]},
                    "purpose": {"type": "string"},
                    "version": {"type": ["string", "integer", "number"]},
                    "related_notes": {"type": "array", "items": {"type": "string"}},
                    "groups": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["name"],
                            "properties": {
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                            },
                        },
                    },
                    "characteristic_element_set": {
                        "type": "array",
                        "items": {"$ref": "#/$defs/element"},
                    },
                },
                "additionalProperties": True,
            },
            "element": {
                "type": "object",
                "required": ["name", "value_set"],
                "properties": {
                    "name": {"type": "string"},
                    "category": {"type": "string"},
                    "description": {"type": "string"},
                    "assignment_rule": {"type": "string"},
                    "scale": {"enum": ["nominal", "ordinal"]},
                    "value_set": {
                        "type": "array",
                        "minItems": 1,
                        "items": {"type": "string"},
                    },
                },
                "additionalProperties": False,
            },
        },
    }


def profile_schema(
    stem: str,
    title: str,
    description: str,
    systems: list[dict],
    container: dict,
) -> dict:
    """A profile store schema: container of entries, each entry -> system -> values.

    ``container`` is the JSON Schema of one entry (a country or an
    organization) minus its ``profiles`` property; the system properties are
    generated from ``systems`` so every element and value set is enumerated.
    """
    entry = dict(container)
    entry["minProperties"] = 1
    entry["additionalProperties"] = False
    entry["properties"] = dict(entry.get("properties") or {})
    entry["properties"]["profiles"] = {
        "type": "object",
        "description": "One value per characteristic element, per representation system.",
        "additionalProperties": False,
        "properties": {
            system["name"]: {"$ref": f"#/$defs/{system['name']}"} for system in systems
        },
    }
    defs = {system["name"]: system_schema(system) for system in systems}
    return {
        "$schema": DRAFT,
        "$id": SCHEMA_ID + f"{stem}.schema.json",
        "title": title,
        "description": description,
        "type": "object",
        "required": ["meta", "organizations"],
        "properties": {
            "meta": {
                "type": "object",
                "required": ["title", "version"],
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "version": {"type": ["string", "integer", "number"]},
                    "countries": {"type": "array"},
                },
            },
            "organizations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["id", "name"],
                    "properties": entry["properties"],
                    "additionalProperties": False,
                },
            },
        },
        "additionalProperties": False,
        "$defs": defs,
    }


def government_schema(stem: str, data: dict, systems: list[dict]) -> dict:
    return {
        "$schema": DRAFT,
        "$id": SCHEMA_ID + f"{stem}.schema.json",
        "title": (data.get("meta") or {}).get("title") or "Government Representation",
        "description": (
            "Assignment profiles of governments under the comparative representation "
            "systems: country name -> system -> characteristic element -> value."
        ),
        "type": "object",
        "required": ["meta", "countries"],
        "properties": {
            "meta": {
                "type": "object",
                "required": ["title", "version", "systems"],
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "version": {"type": ["string", "integer", "number"]},
                    "systems": {
                        "type": "object",
                        "description": "Version of each representation system the profiles were read under.",
                        "additionalProperties": {
                            "type": ["string", "integer", "number"]
                        },
                    },
                },
                "additionalProperties": False,
            },
            "countries": {
                "type": "object",
                "description": "Keyed by country name; a country carries any subset of the systems.",
                "additionalProperties": {
                    "type": "object",
                    "minProperties": 1,
                    "additionalProperties": False,
                    "properties": {
                        system["name"]: {"$ref": f"#/$defs/{system['name']}"}
                        for system in systems
                    },
                },
            },
        },
        "additionalProperties": False,
        "$defs": {system["name"]: system_schema(system) for system in systems},
    }


def main() -> int:
    gov = load(GOV_SYSTEMS)
    org = load(ORG_SYSTEMS)

    write(GOV_SYSTEMS, system_catalogue_schema(GOV_SYSTEMS, gov))
    write(ORG_SYSTEMS, system_catalogue_schema(ORG_SYSTEMS, org))

    gov_profiles = load(GOV_PROFILES)
    write(GOV_PROFILES, government_schema(GOV_PROFILES, gov_profiles, gov["systems"]))

    org_profiles = load(ORG_PROFILES)
    write(
        ORG_PROFILES,
        profile_schema(
            ORG_PROFILES,
            (org_profiles.get("meta") or {}).get("title", "Public Organization Representation"),
            "Organization profiles under the comparative representation systems.",
            org["systems"],
            {
                "properties": {
                    "id": {"type": "string"},
                    "country": {"type": "string"},
                    "name": {"type": "string"},
                    "mandate": {"type": "string"},
                    "confidence": {"enum": ["high", "medium", "low"]},
                }
            },
        ),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
