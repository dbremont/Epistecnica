#!/usr/bin/env python3
"""Fail when a catalog page hardcodes corpus content.

The three catalogs (notes, courses, documents) are generic renderers over
the generated corpus indexes: every card, directory, and link they show
must come from `data/index.json`, `data/links.json`, or the corpus files
those name. A literal corpus entry, a per-directory special case, or a
baked-in artifact href means the listing has stopped reflecting the data —
the defect this check exists to prevent (e.g. the retired hardcoded atlas
card in the notes catalog).

Forbidden in src/{note,course,document}/app/index.html:

- per-directory special cases:  state.dir === '<name>'
- literal corpus artifact paths: 'data/<corpus>/...' or "data/<corpus>/..."
  (`data/index.json` and `data/links.json` are index fetches, not
  entries, and stay allowed)

To surface something, put it in the data (the indexer, `links.json`) or
write it in the docs surface — never in the viewer code.

Usage: python3 bin/check_catalog_literals.py
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAGES = [
    REPO / 'src' / 'note' / 'app' / 'index.html',
    REPO / 'src' / 'course' / 'app' / 'index.html',
    REPO / 'src' / 'document' / 'app' / 'index.html',
]

DIR_SPECIAL = re.compile(r"state\.dir\s*===?\s*['\"][^'\"]+['\"]")
CORPUS_PATH = re.compile(r"['\"]data/[A-Za-z0-9_.-]+/[^'\"]+['\"]")


def main():
    errors = []
    for page in PAGES:
        if not page.is_file():
            errors.append(f'{page.relative_to(REPO)}: missing')
            continue
        for lineno, line in enumerate(
                page.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            where = f'{page.relative_to(REPO)}:{lineno}'
            if DIR_SPECIAL.search(line):
                errors.append(f'{where}: hardcoded directory special case '
                              f'({line.strip()[:90]})')
            if CORPUS_PATH.search(line):
                errors.append(f'{where}: literal corpus path '
                              f'({line.strip()[:90]})')

    if errors:
        print(f'[catalog] FAIL: {len(errors)} hardcoded corpus reference(s)',
              file=sys.stderr)
        for err in errors:
            print('  -', err, file=sys.stderr)
        print('  catalogs render data: put entries in data/index.json or '
              'data/links.json, not in the page.', file=sys.stderr)
        return 1

    print(f'[catalog] ok: {len(PAGES)} catalog pages render only indexed data')
    return 0


if __name__ == '__main__':
    sys.exit(main())
