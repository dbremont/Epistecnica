#!/usr/bin/env python3
"""Validate the technica atlas store (data/technica/meta/atlas.json).

The store is derived from the decomposition tables of the technica notes
(src/note/bin/build_technica_atlas.py), so this checker validates the
merged forest, not the corpus layout:

- header fields present; exactly one root, typed;
- node schema: label, kind (root|grouping|instance), description;
- grouping nodes carry a type and children;
- sibling labels unique (they key the atlas label paths);
- every non-root node names at least one source note — the notes whose
  tables define it — and every source exists under technica/;
- a `note` link, when present, resolves to an existing corpus note;
- declared stats match the tree (plus the table/row counters).

Usage: python3 src/note/bin/atlas_check.py
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATA = REPO / 'src' / 'note' / 'app' / 'data'
STORE = DATA / 'technica' / 'meta' / 'atlas.json'

KINDS = {'root', 'grouping', 'instance'}
HEADER = ('title', 'generated', 'source', 'guide', 'note', 'stats', 'roots')
COUNTERS = ('nodes', 'groupings', 'instances', 'maxDepth', 'branches')

errors = []


def err(msg):
    errors.append(msg)


def check_note(here, path, label):
    if not isinstance(path, str) or not path:
        err(f'{here}: {label} is not a path')
        return
    if not path.startswith('technica/') or not path.endswith('.md'):
        err(f'{here}: {label} {path!r} is not a technica note')
    elif not (DATA / path).is_file():
        err(f'{here}: {label} {path!r} does not exist')


def walk(node, path, depth, stats, root=False):
    if not isinstance(node, dict):
        err(f'{path}: node is not an object')
        return
    label = node.get('label')
    if not label or not isinstance(label, str):
        err(f'{path}: missing label')
        label = '?'
    here = f'{path} → {label}' if path else label

    kind = node.get('kind')
    if kind not in KINDS:
        err(f'{here}: bad kind {kind!r}')
    if not isinstance(node.get('description', ''), str):
        err(f'{here}: description is not a string')

    children = node.get('children') or []
    if not isinstance(children, list):
        err(f'{here}: children is not a list')
        children = []

    stats['nodes'] += 1
    stats['maxDepth'] = max(stats['maxDepth'], depth)

    if kind == 'root':
        if root is False and path:
            err(f'{here}: a second root node')
        if not node.get('type'):
            err(f'{here}: root missing type')
        if not children:
            err(f'{here}: root has no branches')
    else:
        sources = node.get('sources')
        if not isinstance(sources, list) or not sources:
            err(f'{here}: missing sources (the notes whose tables define it)')
        else:
            for source in sources:
                check_note(here, source, 'source')
        if 'note' in node:
            check_note(here, node.get('note'), 'note')
        if kind == 'grouping':
            stats['groupings'] += 1
            if not node.get('type'):
                err(f'{here}: grouping missing type')
            if not children:
                err(f'{here}: grouping has no children')
    if kind == 'instance':
        stats['instances'] += 1

    names = [c.get('label') for c in children if isinstance(c, dict)]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        err(f'{here}: duplicate sibling labels {dupes}')

    for child in children:
        walk(child, here, depth + 1, stats)


def main():
    if not STORE.is_file():
        print(f'[atlas] FAIL: {STORE.relative_to(REPO)} missing — '
              'run make atlas-index', file=sys.stderr)
        return 1
    data = json.load(open(STORE))

    for k in HEADER:
        if k not in data:
            err(f'header missing {k!r}')
    roots = data.get('roots')
    if not isinstance(roots, list) or len(roots) != 1:
        err('roots must be a list with exactly one synthetic root')
        roots = roots if isinstance(roots, list) else []

    stats = {'nodes': 0, 'groupings': 0, 'instances': 0, 'maxDepth': 0}
    for root in roots:
        walk(root, '', 1, stats, root=True)
    stats['branches'] = len((roots or [{}])[0].get('children', []))

    declared = data.get('stats', {})
    for k in COUNTERS:
        if declared.get(k) != stats[k]:
            err(f'stats.{k}: declared {declared.get(k)!r} != actual {stats[k]}')
    for k in ('tables', 'rows'):
        if not isinstance(declared.get(k), int) or declared.get(k) < 1:
            err(f'stats.{k}: missing or not a positive count')

    if errors:
        print(f'[atlas] FAIL: {len(errors)} problem(s)', file=sys.stderr)
        for e in errors[:40]:
            print('  -', e, file=sys.stderr)
        if len(errors) > 40:
            print(f'  … and {len(errors) - 40} more', file=sys.stderr)
        return 1

    print(f"[atlas] ok: {declared['rows']} table rows from "
          f"{declared['tables']} tables -> {stats['nodes']} nodes "
          f"({stats['groupings']} groupings, {stats['instances']} instances), "
          f"{stats['branches']} branches, depth {stats['maxDepth']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
