#!/usr/bin/env python3
"""Validate the technical-object taxonomy store.

The taxonomy is authored data carried in the atlas store
(src/corpus/notes/technica/atlas.json → `taxonomy`), seeded from the
tracked archive src/corpus/notes/technica/atlas-taxonomy.json when the
store is first built; technical-object-taxonomy.html reads it from there. It classifies the technical objects the technica corpus decomposes —
object domain → object kind (the guide's own type) → class → object — and
gives each object its economic reading (the good kinds of
social/good/good.md), so the goods catalogue and the technical-object
catalogue can be read against each other.

Checks:

- the atlas store carries a non-empty `taxonomy` section (a missing one
  fails with "run make atlas-index");
- every node: id, label, level, parent; ids unique;
- every domain is a root (parent null) and every other node's parent
  exists — a parent cycle or an orphan fails;
- level chain: domain (1) → kind (2) → class (3) → object (4), no skip,
  no node without children except objects;
- `kind` (object-kind nodes) is a technical-element type of the canonical
  technica guide;
- `guide` on an object is one of the types the object is typed as
  (object, or object plus a `readable as` reading);
- `good` is a comma-separated selection of the good.md classification
  tokens, one value per axis (Excludability & Rivalry, Durability,
  Production Process, Use);
- `hs` matches an HS heading/subheading shape.
- `atlas`, when present, resolves to a row of the same store's forest;
- `note`, when present, resolves to a technica note under the corpus.

Usage: python3 bin/object_taxonomy_check.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / 'src' / 'corpus' / 'notes'
ATLAS = NOTES / 'technica' / 'atlas.json'
ARCHIVE = NOTES / 'technica' / 'atlas-taxonomy.json'

LEVELS = [None, 'domain', 'kind', 'class', 'object']
AXES = [
    {'Private', 'Public', 'Club', 'Common-pool'},
    {'Durable', 'Non-durable'},
    {'Capital', 'Consumer'},
    {'Intermediate', 'Final'},
]
GOOD_TOKENS = set().union(*AXES)

# Technical-element types of the canonical guide
# (philosophia-artium-technicarum-et-operis.md, `Permitted Link Forms`).
OBJECT_TYPES = {
    'Production Technical Object',
    'Physical Production Technical Object',
    'Production Virtual Technical Object',
    'Constitutive Technical Object',
    'Production Support',
    'Production Tool',
    'Production Instrument',
    'Production Equipment',
    'Production Facility',
    'Machine',
    'Production Technical System',
    'Producing Technical Element',
    'Material Good Producer',
    'Energy Good Producer',
    'Information Good Producer',
    'Service Good Producer',
}

HS = re.compile(r'^\d{4}(\.\d{2})?$')

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def load():
    """(taxonomy nodes, atlas paths) from the generated atlas store.

    The taxonomy lives in the store's `taxonomy` section, beside the forest,
    so one read serves both the classification and the path cross-check.
    Returns (None, None) when the store is absent or unusable.
    """
    if not ATLAS.is_file():
        err(f'{ATLAS.relative_to(REPO)}: missing — run make atlas-index')
        return None, None
    try:
        data = json.loads(ATLAS.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        err(f'{ATLAS.relative_to(REPO)}: invalid JSON ({exc}) — run make atlas-index')
        return None, None

    paths = set()

    def walk(node, path):
        here = path + [node.get('label', '?')]
        paths.add(' → '.join(here))
        for child in node.get('children') or []:
            walk(child, here)

    for root in data.get('roots') or []:
        walk(root, [])

    tax = data.get('taxonomy')
    if not isinstance(tax, dict) or not isinstance(tax.get('nodes'), list):
        err(f'{ATLAS.relative_to(REPO)}: no taxonomy section — run make atlas-index')
        return None, paths
    nodes = tax['nodes']
    if not nodes:
        err(f'{ATLAS.relative_to(REPO)}: taxonomy section is empty — '
            'run make atlas-index')
        return None, paths

    # The tracked archive is the authoring surface: it must agree with the
    # store, or `make atlas-index` has not been run since the last edit.
    if ARCHIVE.is_file():
        try:
            authored = json.loads(ARCHIVE.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            err(f'{ARCHIVE.relative_to(REPO)}: invalid JSON ({exc})')
        else:
            if authored != nodes:
                err(f'{ATLAS.relative_to(REPO)}: taxonomy section is stale — '
                    f'it differs from {ARCHIVE.relative_to(REPO)}; '
                    'run make atlas-index')
    else:
        warnings.append(f'{ARCHIVE.relative_to(REPO)}: missing — the authored '
                        'taxonomy archive is not in the repo')
    return nodes, paths


def check_good(here, value):
    if not isinstance(value, str) or not value.strip():
        err(f'{here}: good is empty')
        return
    tokens = [t.strip() for t in value.split(',') if t.strip()]
    if len(tokens) != len(AXES):
        err(f'{here}: good {value!r} names {len(tokens)} value(s), '
            f'not one per axis ({len(AXES)})')
        return
    for token, axis in zip(tokens, AXES):
        if token not in axis:
            err(f'{here}: good value {token!r} is not in {{{", ".join(sorted(axis))}}}')


def check_guide(here, value):
    if not isinstance(value, str) or not value.strip():
        err(f'{here}: guide is empty')
        return
    parts = [p.strip() for p in value.split(',')]
    bad = [p for p in parts
           if p not in OBJECT_TYPES and not p.startswith('readable as ')]
    if bad:
        err(f'{here}: guide names unknown type(s): {", ".join(bad)}')
    primary = parts[0] if parts else ''
    if primary not in OBJECT_TYPES:
        err(f'{here}: guide primary {primary!r} is not a technical-element type')


def check_link(here, value):
    if not isinstance(value, str) or not value:
        err(f'{here}: link is empty')
        return
    if not value.startswith('technica/') or not value.endswith('.md'):
        err(f'{here}: link {value!r} is not a technica note')
    elif not (NOTES / value).is_file():
        err(f'{here}: link {value!r} does not exist')


def main():
    nodes, paths = load()
    if nodes is None:
        for w in warnings:
            print(f'[object-taxonomy] warn: {w}', file=sys.stderr)
        for e in errors:
            print(f'[object-taxonomy] {e}', file=sys.stderr)
        return 1
    if not isinstance(nodes, list) or not nodes:
        err('taxonomy section is not a non-empty list')
        for e in errors:
            print(f'[object-taxonomy] {e}', file=sys.stderr)
        return 1
    by_id = {}
    depth = {}

    for i, node in enumerate(nodes):
        here = f'[{i}]'
        if not isinstance(node, dict):
            err(f'{here}: node is not an object')
            continue
        nid = node.get('id')
        if not isinstance(nid, str) or not nid:
            err(f'{here}: missing id')
            continue
        here = f'{nid}'
        if nid in by_id:
            err(f'{here}: duplicate id')
            continue
        by_id[nid] = node
        label = node.get('label')
        if not isinstance(label, str) or not label.strip():
            err(f'{here}: missing label')
        level = node.get('level')
        if level not in LEVELS[1:]:
            err(f'{here}: level {level!r} is not one of {LEVELS[1:]}')
        if 'parent' not in node:
            err(f'{here}: missing parent (use null for the root)')

    # Single root + parent chain.
    roots = [n for n in by_id.values() if n.get('parent') is None]
    if len(roots) < 2:
        err(f'expected at least two domain roots (parent null), found '
            f'{len(roots)}: {", ".join(n["id"] for n in roots)}')
    for node in roots:
        if node.get('level') != 'domain':
            err(f'{node.get("id")}: root is a {node.get("level")!r}, not a domain')
    for nid, node in by_id.items():
        parent = node.get('parent')
        depth[nid] = None
        if parent is not None and parent not in by_id:
            err(f'{nid}: parent {parent!r} does not exist')

    # Resolve depth, detecting cycles. A domain is its own level 1; every
    # other node is one level below its nearest domain ancestor.
    def depth_of(nid):
        if depth.get(nid) is not None:
            return depth[nid]
        node = by_id[nid]
        if node.get('parent') is None:
            depth[nid] = 0        # domain: level = depth + 1
            return 0
        parent = node['parent']
        if depth.get(parent) == -99:
            err(f'{nid}: parent cycle through {parent!r}')
            depth[nid] = -1
            return -1
        if depth.get(parent) is None:
            depth[parent] = -99      # in progress: a revisit is a cycle
        d = depth_of(parent)
        depth[nid] = -1 if d < 0 else d + 1
        return depth[nid]

    for nid in by_id:
        depth_of(nid)

    children = {}
    for nid, node in by_id.items():
        parent = node.get('parent')
        if parent in by_id:
            children.setdefault(parent, []).append(nid)

    for nid, node in by_id.items():
        d = depth.get(nid)
        level = node.get('level')
        if d is not None and d >= 0 and level in LEVELS[1:]:
            if LEVELS[d + 1] != level:
                err(f'{nid}: level {level!r} does not match its tree depth '
                    f'(expected {LEVELS[d + 1]!r})')
        kids = children.get(nid, [])
        if level == 'object':
            if kids:
                err(f'{nid}: object node has children')
            check_guide(nid, node.get('guide'))
            check_good(nid, node.get('good'))
            hs = node.get('hs')
            if hs is not None and not (isinstance(hs, str) and HS.match(hs)):
                err(f'{nid}: hs {hs!r} is not an HS heading/subheading')
            link = node.get('link')
            if link is not None:
                check_link(nid, link)
            atlas = node.get('atlas')
            if atlas is not None:
                if not isinstance(atlas, str) or not atlas:
                    err(f'{nid}: atlas is not a path')
                elif paths is not None and atlas not in paths:
                    err(f'{nid}: atlas path not in the atlas forest: {atlas}')
        else:
            if not kids:
                err(f'{nid}: {level} node has no children')
            if 'guide' in node or 'good' in node or 'hs' in node:
                err(f'{nid}: only object nodes carry guide/good/hs')
        if level == 'kind':
            kind = node.get('kind')
            if kind not in OBJECT_TYPES:
                err(f'{nid}: kind {kind!r} is not a technical-element type '
                    'of the guide')

    # Counts.
    counts = {lv: 0 for lv in LEVELS[1:]}
    for node in by_id.values():
        lv = node.get('level')
        if lv in counts:
            counts[lv] += 1
    if counts['object'] == 0:
        err('no object nodes')
    if not (30 <= counts["object"] <= 400):
        warnings.append(f'{counts["object"]} object nodes — the lean budget '
                        'is 80–110; check the scale is intended')

    for w in warnings:
        print(f'[object-taxonomy] warn: {w}', file=sys.stderr)
    if errors:
        print(f'[object-taxonomy] FAIL: {len(errors)} error(s)', file=sys.stderr)
        for e in errors:
            print('  -', e, file=sys.stderr)
        return 1

    print(f'[object-taxonomy] ok: {len(by_id)} nodes — '
          + ' · '.join(f'{counts[lv]} {lv}' for lv in LEVELS[1:])
          + (' · atlas paths verified' if paths is not None
             else ' · atlas paths skipped'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
