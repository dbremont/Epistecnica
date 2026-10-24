#!/usr/bin/env python3
"""Build the technica atlas store: the Technical Element Forest.

Walks src/note/app/data/technica/ and renders its directory decomposition
plus every corpus note into a forest store (data/technica/atlas/atlas.json),
the store the atlas page (data/technica/atlas/atlas.html) renders.

Node model (REEs-compatible, see epistemica/rees.json):
  root      - the section itself, typed Technical Element Set
  grouping  - a directory, typed from its index note's declared guide type
              (the backticked type in the note's first blockquote), with a
              curated fallback table for sections that predate the pattern
  instance  - a corpus note: title, description snippet, corpus path, tags

Usage: python3 src/note/bin/build_technica_atlas.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATA = REPO / 'src' / 'note' / 'app' / 'data'
TECH = DATA / 'technica'
INDEX = DATA / 'index.json'
OUT = TECH / 'atlas' / 'atlas.json'

GUIDE = ('https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/'
         'main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md')

# Section roots: curated types (the guide type where the dir literally is
# one, otherwise the section's own designation).
ROOT_TYPES = {
    'ais': 'Technical Domain',
    'computation': 'Technical Domain',
    'cto': 'Constitutive Technical Object',
    'op': 'Technical Operation',
    'pto': 'Production Technical Object',
    'robotic-system': 'Production Technical System',
}

# Index notes not named <dir>.md.
ALT_INDEX = {
    'computation': 'computacion.md',
    'cto': 'readme.md',
    'op': 'readme.md',
    'pto': 'readme.md',
}

# Fallback grouping types for index notes that declare no backticked type.
DIR_TYPES = {
    'theory': 'Technical Theory',
    'evaluation': 'Technical Evaluation',
    'transformer': 'Technical Architecture',
}
FALLBACK_TYPE = 'Technical Element Grouping'

DECLARED = re.compile(r'^\s*>\s*`([^`]+)`')
BLOCK = re.compile(r'^((?:\s*>.*\n?)+)', re.M)
SNIP = re.compile(r'\s+')

stats = {'nodes': 0, 'groupings': 0, 'instances': 0, 'maxDepth': 0}


def read(path):
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return ''


def title_of(text, fallback):
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else fallback


def strip_md(s, limit=240):
    s = re.sub(r'\$\$?.*?\$\$?', ' ', s)
    s = re.sub(r'```.*?```', ' ', s, flags=re.S)
    s = re.sub(r'[#*_`>|\\-]+', ' ', s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = SNIP.sub(' ', s).strip()
    if len(s) > limit:
        s = s[:limit].rsplit(' ', 1)[0] + '…'
    return s


def description_of(text):
    """First blockquote, else first prose paragraph, clipped."""
    m = re.search(r'^\s*>\s*(.+)$', text, re.M)
    if m and not set(m.group(1)) <= set('. …>-—'):
        return strip_md(m.group(1))
    body = re.sub(r'^---$.*?^---$', '', text, count=1, flags=re.S | re.M)
    body = re.sub(r'^#.*$', '', body, flags=re.M)
    for para in body.split('\n\n'):
        p = para.strip()
        if p and not p.startswith(('>', '|', '- [', '!')):
            return strip_md(p)
    return ''


def declared_type(text):
    """The guide type an index note declares in its first blockquote."""
    m = BLOCK.search(text)
    d = DECLARED.search(m.group(1)) if m else None
    return d.group(1).strip() if d else None


def index_note(d, alt=False):
    f = d / (ALT_INDEX.get(d.name, d.name + '.md'))
    return f if f.is_file() else None


def instance_node(md, notes, depth):
    rel = str(md.relative_to(DATA))
    meta = notes.get(rel, {})
    text = meta.get('text') or read(md)
    node = {
        'label': meta.get('title') or title_of(text, md.stem),
        'kind': 'instance',
        'description': strip_md(text),
        'path': rel,
    }
    tags = meta.get('tags') or []
    if tags:
        node['tags'] = tags
    stats['nodes'] += 1
    stats['instances'] += 1
    stats['maxDepth'] = max(stats['maxDepth'], depth)
    return node


def dedupe_labels(children):
    """Sibling labels must be unique (they key the atlas's label paths).

    On collision, instances take their corpus stem in parentheses — the
    stem is unique within its directory by construction.
    """
    counts = {}
    for c in children:
        counts[c['label']] = counts.get(c['label'], 0) + 1
    for c in children:
        if counts[c['label']] > 1 and c['kind'] == 'instance':
            stem = Path(c['path']).stem
            if stem != c['label']:
                c['label'] += ' (' + stem + ')'
    taken = set()
    for c in children:
        label, n = c['label'], 2
        while c['label'] in taken:
            c['label'] = f'{label} ({n})'
            n += 1
        taken.add(c['label'])


def grouping_node(d, base, notes, depth, is_root=False):
    note = index_note(d)
    text = read(note) if note else ''
    rel_dir = str(d.relative_to(TECH))
    label = 'Technica' if is_root else title_of(text, d.name)
    if is_root:
        typ = 'Technical Element Set'
    else:
        typ = (declared_type(text)
               or ROOT_TYPES.get(rel_dir)
               or DIR_TYPES.get(rel_dir)
               or DIR_TYPES.get(d.name)
               or FALLBACK_TYPE)
    node = {
        'label': label,
        'kind': 'root' if is_root else 'grouping',
        'type': typ,
        'description': description_of(text) or strip_md(
            'The ' + label + ' branch of the technica corpus.'),
        'children': [],
    }

    for sub in sorted([p for p in d.iterdir() if p.is_dir()
                       and not p.name.startswith('.')]):
        if is_root and sub.name == OUT.parent.name:
            continue  # the store's own dir is not a corpus grouping
        child = grouping_node(sub, base, notes, depth + 1)
        if child:
            node['children'].append(child)
    for md in sorted(d.glob('*.md')):
        if note and md == note:
            continue  # the index note speaks for its directory
        node['children'].append(instance_node(md, notes, depth + 1))
    dedupe_labels(node['children'])
    if not is_root and not node['children']:
        return None  # a grouping with no corpus notes is not in the forest
    stats['nodes'] += 1
    if not is_root:
        stats['groupings'] += 1
    stats['maxDepth'] = max(stats['maxDepth'], depth)
    return node


def main():
    if not INDEX.is_file():
        print('atlas: index.json missing — run make notes-index first',
              file=sys.stderr)
        return 1
    notes = {n['path']: n for n in json.load(open(INDEX))['notes']
             if n.get('path', '').startswith('technica/')}

    root = grouping_node(TECH, TECH, notes, 1, is_root=True)
    branches = len(root['children'])

    store = {
        'title': 'Technical Element Forest',
        'abbr': 'TEF',
        'generated': date.today().isoformat(),
        'source': 'generated from the technica corpus directory tree '
                  '(src/note/app/data/technica)',
        'guide': GUIDE,
        'note': 'technica/atlas/atlas.md',
        'stats': {**stats, 'branches': branches},
        'roots': [root],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(store, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(f"atlas: {stats['nodes']} nodes "
          f"({stats['groupings']} groupings, {stats['instances']} instances), "
          f"{branches} branches, depth {stats['maxDepth']} -> "
          f"{OUT.relative_to(REPO)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
