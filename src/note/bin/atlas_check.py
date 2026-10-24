#!/usr/bin/env python3
"""Validate the technica atlas store (data/technica/atlas/atlas.json).

Checks: header fields; node schema (label/kind); grouping types non-empty;
sibling labels unique; instances leaf-only with an existing corpus path
under technica/; stats consistent with the tree.

Usage: python3 src/note/bin/atlas_check.py
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATA = REPO / 'src' / 'note' / 'app' / 'data'
STORE = DATA / 'technica' / 'atlas' / 'atlas.json'

KINDS = {'root', 'grouping', 'instance'}
HEADER = ('title', 'generated', 'source', 'guide', 'note', 'stats', 'roots')

errors = []


def err(msg):
    errors.append(msg)


def walk(node, path, depth, stats, seen_paths):
    if not isinstance(node, dict):
        err(f'{path}: node is not an object')
        return
    label = node.get('label')
    if not label:
        err(f'{path}: missing label')
        label = '?'
    here = f'{path} → {label}' if path else label

    kind = node.get('kind')
    if kind not in KINDS:
        err(f'{here}: bad kind {kind!r}')
    children = node.get('children') or []

    stats['nodes'] += 1
    stats['maxDepth'] = max(stats['maxDepth'], depth)
    if kind == 'root':
        if not node.get('type'):
            err(f'{here}: root missing type')
    elif kind == 'grouping':
        stats['groupings'] += 1
        if not node.get('type'):
            err(f'{here}: grouping missing type')
        if not children:
            err(f'{here}: grouping has no children')
        names = [c.get('label') for c in children if isinstance(c, dict)]
        dupes = sorted({n for n in names if names.count(n) > 1})
        if dupes:
            err(f'{here}: duplicate sibling labels {dupes}')
    elif kind == 'instance':
        stats['instances'] += 1
        if children:
            err(f'{here}: instance must be a leaf')
        p = node.get('path')
        if not p:
            err(f'{here}: instance missing corpus path')
        elif not p.startswith('technica/') or not p.endswith('.md'):
            err(f'{here}: path {p!r} not a technica note')
        elif not (DATA / p).is_file():
            err(f'{here}: path {p!r} does not exist')
        elif p in seen_paths:
            err(f'{here}: path {p!r} already used by another instance')
        else:
            seen_paths.add(p)

    for c in children:
        walk(c, here, depth + 1, stats, seen_paths)


def main():
    if not STORE.is_file():
        print(f'[atlas] FAIL: {STORE.relative_to(REPO)} missing — '
              'run make atlas-index', file=sys.stderr)
        return 1
    data = json.load(open(STORE))

    for k in HEADER:
        if k not in data:
            err(f'header missing {k!r}')
    if not isinstance(data.get('roots'), list) or not data.get('roots'):
        err('roots must be a non-empty list')

    stats = {'nodes': 0, 'groupings': 0, 'instances': 0, 'maxDepth': 0}
    seen_paths = set()
    for r in data.get('roots', []):
        walk(r, '', 1, stats, seen_paths)
    stats['branches'] = len((data.get('roots') or [{}])[0].get('children', []))

    declared = data.get('stats', {})
    for k, v in stats.items():
        if declared.get(k) != v:
            err(f'stats.{k}: declared {declared.get(k)!r} != actual {v}')

    if errors:
        print(f'[atlas] FAIL: {len(errors)} problem(s)', file=sys.stderr)
        for e in errors[:40]:
            print('  -', e, file=sys.stderr)
        if len(errors) > 40:
            print(f'  … and {len(errors) - 40} more', file=sys.stderr)
        return 1

    print(f"[atlas] ok: {stats['nodes']} nodes "
          f"({stats['groupings']} groupings, {stats['instances']} instances), "
          f"{stats['branches']} branches, depth {stats['maxDepth']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
