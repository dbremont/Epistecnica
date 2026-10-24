#!/usr/bin/env python3
"""Build the technica atlas store: the Technical Element Forest.

Parses the decomposition tables of the technica notes — never the
directory layout — and merges them into one forest store
(data/technica/meta/atlas.json), the store the atlas page
(data/technica/meta/atlas.html) renders.

Two table syntaxes live in the corpus and both feed the same trie:

  four-column  | Instance Tree Path | Description | Technical Category |
               | Technical Element Type Tree Path |
               instance paths split on ` > `; the fourth column is a
               backticked type path starting at `(root)`, whose last
               segment types the row's terminal segment. A backticked
               col-1 segment names a type when it belongs to the guide's
               type vocabulary (collected from the type column), and a
               concrete artifact otherwise.

  two-column   | Instance Tree Path | Description |
               epistemic-style paths split on `→` with backticked type
               segments inline; plain segments are instances typed by the
               nearest grouping ancestor.

Node model (REEs-compatible, see epistemica/rees.json):

  root      - one synthetic `Technical Element` node, typed
              Technical Element Set; its children are the table roots
  grouping  - a type segment (backticked in the table)
  instance  - a named technical element; it may carry children (the
              decomposition is recursive), unlike the old file-tree store

Every node records the notes whose tables define it (`sources`), and an
instance whose label matches exactly one corpus note carries that note's
path (`note`). The store is generated data: never hand-edit it.

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
OUT = TECH / 'meta' / 'atlas.json'

GUIDE = ('https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/'
         'main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md')

FOUR = ('| Instance Tree Path | Description | Technical Category | '
        'Technical Element Type Tree Path |')
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


def four_rows(text):
    """Every four-column decomposition row (all table blocks of a note)."""
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        c = cells(line)
        if len(c) == 4 and c[3].startswith('`(root)') \
                and c[0] != 'Instance Tree Path':
            yield c


def two_rows(text):
    """Every two-column `→` decomposition row (all table blocks)."""
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        c = cells(line)
        if len(c) == 2 and ' → ' in c[0] \
                and c[0] != 'Instance Tree Path':
            yield c


def segment(raw, vocabulary):
    """(label, kind) for one instance-path segment.

    Bold marks an instance; a backticked segment is a type grouping when
    its label belongs to the guide type vocabulary, a concrete artifact
    (instance) otherwise. Plain segments are instances.
    """
    s = raw.strip()
    if len(s) > 4 and s.startswith('**') and s.endswith('**'):
        return s[2:-2].strip(), 'instance'
    if len(s) > 2 and s.startswith('`') and s.endswith('`'):
        inner = s[1:-1].strip()
        return inner, ('grouping' if inner in vocabulary else 'instance')
    return s, 'instance'


def type_path(cell):
    """Segments of a fourth-column type path, `(root)` removed."""
    raw = cell.strip()
    if raw.startswith('`') and raw.endswith('`'):
        raw = raw[1:-1]
    return [p.strip() for p in raw.split(' > ')
            if p.strip() and p.strip() != '(root)']


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

        `terminal_type` types the row's last segment (four-column tables);
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
    four_files, two_files = [], []
    for path in sorted(TECH.rglob('*.md')):
        rel = path.relative_to(TECH)
        if 'meta' in rel.parts:
            continue  # meta/ holds the atlas itself, not elements
        text = read(path)
        title = TITLE.search(text)
        notes.append(('technica/' + rel.as_posix(),
                      title.group(1).strip() if title else path.stem,
                      path.stem))
        if FOUR in text:
            four_files.append((path, text))
        elif TWO in text:
            two_files.append((path, text))

    # The guide's type vocabulary, read off the type column itself: a
    # backticked col-1 segment naming one of these is a type grouping.
    vocabulary = set()
    for _, text in four_files:
        for row in four_rows(text):
            vocabulary.update(type_path(row[3]))

    forest = Forest()
    rows = 0
    for path, text in four_files:
        source = 'technica/' + path.relative_to(TECH).as_posix()
        for row in four_rows(text):
            segments = [segment(s, vocabulary) for s in row[0].split(' > ')]
            types = type_path(row[3])
            forest.add(segments, source,
                       terminal_type=types[-1] if types else None,
                       description=strip_md(row[1]))
            rows += 1
    for path, text in two_files:
        source = 'technica/' + path.relative_to(TECH).as_posix()
        for row in two_rows(text):
            segments = [segment(s, vocabulary) for s in row[0].split(' → ')]
            groupings = [label for label, kind in segments[:-1]
                         if kind == 'grouping']
            forest.add(segments, source,
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
    stats['tables'] = len(four_files) + len(two_files)
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
