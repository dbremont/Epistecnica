#!/usr/bin/env python3
"""Build the technica atlas store: the Technical Element Forest.

Parses the decomposition tables of the technica notes — never the
directory layout — and merges them into one forest store
(data/technica/meta/atlas.json), the store the atlas page
(data/technica/meta/atlas.html) renders.

The table form is the guide's canonical one:

  | Instance Tree Path | Description |

Paths split on `→`; backticked segments are type groupings, plain segments
are instances typed by the nearest grouping ancestor.

Node model (EES-compatible, see epistemica/ees.json):

  root      - one synthetic `Technical Element` node, typed
              Technical Element Set; its children are the table roots
  grouping  - a type segment (backticked in the table)
  instance  - a named technical element; it may carry children (the
              decomposition is recursive), unlike the old file-tree store

Every node records the notes whose tables define it (`sources`), and an
instance whose label matches exactly one corpus note carries that note's
path (`note`). The store is generated data: never hand-edit it.

Usage: python3 bin/build_technica_atlas.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / 'src' / 'note' / 'app' / 'data'
TECH = DATA / 'technica'
OUT = TECH / 'meta' / 'atlas.json'

GUIDE = ('https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/'
         'main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md')

TWO = '| Instance Tree Path | Description |'
ROOT_LABEL = 'Technical Element'
ROOT_TYPE = 'Technical Element Set'
SNIP = re.compile(r'\s+')
TITLE = re.compile(r'^#\s+(.+)$', re.M)
CODE = re.compile(r'`([^`]*)`')
MATH = re.compile(r'\$\$?.*?\$\$?')
LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
SLUG = re.compile(r'[^a-z0-9]+')


def read(path):
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return ''


def strip_md(s):
    s = MATH.sub(' ', s)
    s = CODE.sub(r'\1', s)
    s = LINK.sub(r'\1', s)
    s = SNIP.sub(' ', s).strip()
    return s


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


SEG_TOKEN = re.compile(r'`([^`]*)`|([^`]+)')
SEG_LINK = re.compile(r'^\(\s*(?:→|->)\s*(.+?)\s*\)$')
SEG_LINKED = re.compile(r'`\(\s*(?:→|->)')


def two_rows(text):
    """Every two-column decomposition row (all table blocks)."""
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        c = cells(line)
        if len(c) != 2 or c[0] == 'Instance Tree Path':
            continue
        if ' → ' in c[0] or SEG_LINKED.search(c[0]):
            yield c


def segments(cell):
    """[(label, kind)] for one path cell, in either accepted grammar.

    Old form: `A` → B → `C`.
    New form: `Technical Element` `(→ Kind)` `A` `(→ Instance)` B — the
    leading root node and the relationship labels are dropped here: the
    forest already roots at `Technical Element`, and typing reads from the
    type segments.
    """
    cell = cell.strip()
    if SEG_LINKED.search(cell):
        segs = []
        for match in SEG_TOKEN.finditer(cell):
            code, plain = match.group(1), match.group(2)
            if code is not None:
                inner = code.strip()
                if SEG_LINK.match(inner):
                    continue  # relationship label, not a node
                segs.append((inner, 'grouping'))
            else:
                text = plain.strip()
                if text:
                    segs.append((text, 'instance'))
        if segs and segs[0] == ('Technical Element', 'grouping'):
            segs = segs[1:]
        return segs
    return [segment(s) for s in cell.split(' → ')]



def segment(raw):
    """(label, kind) for one instance-path segment.

    A backticked segment is a type grouping; a plain segment is an
    instance.
    """
    s = raw.strip()
    if len(s) > 2 and s.startswith('`') and s.endswith('`'):
        return s[1:-1].strip(), 'grouping'
    return s.replace('**', '').replace('`', '').strip(), 'instance'


def slug(s):
    return SLUG.sub(' ', s.lower()).strip()


class Forest:
    """One trie over every instance path of every decomposition table."""

    def __init__(self):
        self.root = {
            'label': ROOT_LABEL,
            'kind': 'root',
            'type': ROOT_TYPE,
            'description': ('The complete, ever-expanding forest of technical '
                            'elements: every decomposition table of the '
                            'technica corpus merged into one instance tree.'),
            'sources': [],
            'children': [],
        }

    def node(self, parent, label):
        """Child of `parent` named `label`, created on first sight."""
        for child in parent['children']:
            if child['label'] == label:
                return child
        node = {'label': label, 'kind': 'instance', 'description': '',
                'sources': set(), 'children': []}
        parent['children'].append(node)
        return node

    def add(self, segments, source, terminal_type=None, description=''):
        """Add one table row: `segments` = [(label, kind), ...] from the root.

        `terminal_type` is the nearest grouping label (two-column tables);
        intermediate segments inherit the nearest ancestor's type. Type
        groupings are typed by their own label.
        """
        parent = self.root
        inherited = None
        for i, (label, kind) in enumerate(segments):
            if not label:
                continue
            node = self.node(parent, label)
            node['sources'].add(source)
            last = i == len(segments) - 1
            if kind == 'grouping':
                node['kind'] = 'grouping'
                node['type'] = label
            elif not node.get('type'):
                node['type'] = (terminal_type if last and terminal_type
                                else inherited)
            inherited = node.get('type') or inherited
            if last and description and not node['description']:
                node['description'] = description
            parent = node

    def finish(self):
        """Sort the branches, freeze sources, type the root's tree."""
        self.root['children'].sort(key=lambda n: n['label'].lower())
        self._freeze(self.root)

    def _freeze(self, node):
        if isinstance(node.get('sources'), set):
            node['sources'] = sorted(node['sources'])
        if node['kind'] == 'grouping' and not node['description']:
            node['description'] = 'Type grouping: ' + node['label'] + '.'
        for child in node['children']:
            self._freeze(child)

    def walk(self, node=None, depth=1):
        node = node or self.root
        yield node, depth
        for child in node['children']:
            yield from self.walk(child, depth + 1)


def note_links(notes):
    """Label → corpus note path, only for unambiguous title/slug matches."""
    titles, stems = {}, {}
    for path, title, stem in notes:
        titles.setdefault(slug(title), set()).add(path)
        stems.setdefault(slug(stem), set()).add(path)

    def resolve(label):
        key = slug(label)
        found = titles.get(key) or stems.get(key) or set()
        return next(iter(found)) if len(found) == 1 else None

    return resolve


def main():
    if not TECH.is_dir():
        print('atlas: technica corpus missing', file=sys.stderr)
        return 1

    notes = []
    table_files = []
    for path in sorted(TECH.rglob('*.md')):
        rel = path.relative_to(TECH)
        if 'meta' in rel.parts:
            continue  # meta/ holds the atlas itself, not elements
        text = read(path)
        title = TITLE.search(text)
        notes.append(('technica/' + rel.as_posix(),
                      title.group(1).strip() if title else path.stem,
                      path.stem))
        if TWO in text:
            table_files.append((path, text))

    forest = Forest()
    rows = 0
    for path, text in table_files:
        source = 'technica/' + path.relative_to(TECH).as_posix()
        for row in two_rows(text):
            segs = segments(row[0])
            groupings = [label for label, kind in segs[:-1]
                         if kind == 'grouping']
            forest.add(segs, source,
                       terminal_type=(groupings[-1] if groupings else None),
                       description=strip_md(row[1]))
            rows += 1

    if not forest.root['children']:
        print('atlas: no decomposition tables found under technica/',
              file=sys.stderr)
        return 1

    forest.finish()

    resolve = note_links(notes)
    linked = 0
    for node, _ in forest.walk():
        if node['kind'] != 'instance':
            continue
        note = resolve(node['label'])
        if note:
            node['note'] = note
            linked += 1

    stats = {'nodes': 0, 'groupings': 0, 'instances': 0, 'maxDepth': 0}
    for node, depth in forest.walk():
        stats['nodes'] += 1
        stats['maxDepth'] = max(stats['maxDepth'], depth)
        if node['kind'] == 'grouping':
            stats['groupings'] += 1
        elif node['kind'] == 'instance':
            stats['instances'] += 1
    stats['branches'] = len(forest.root['children'])
    stats['tables'] = len(table_files)
    stats['rows'] = rows

    store = {
        'title': 'Technical Element Forest',
        'abbr': 'TEF',
        'generated': date.today().isoformat(),
        'source': 'generated from the decomposition tables of the technica '
                  'corpus (src/note/app/data/technica, meta/ excluded)',
        'guide': GUIDE,
        'note': 'technica/meta/atlas.md',
        'stats': stats,
        'roots': [forest.root],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(store, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(f"atlas: {stats['rows']} table rows from {stats['tables']} tables "
          f"-> {stats['nodes']} nodes ({stats['groupings']} groupings, "
          f"{stats['instances']} instances), {stats['branches']} branches, "
          f"depth {stats['maxDepth']}, {linked} note links -> "
          f"{OUT.relative_to(REPO)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
