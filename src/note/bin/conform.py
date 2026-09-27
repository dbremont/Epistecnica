#!/usr/bin/env python3
"""
Decomposition-table conformance checker.

Verifies that every `Instance Tree Path` table in the given technical
notes adheres to the decomposition standards owned by
src/note/app/notes/general/philosophia-artium-technicarum-et-operis.md:

- every fourth-column type path resolves to a Recursive-view grammar path
  (`Technical Element Set`-prefixed, spine levels never skipped, no
  `...`/`{...}` wildcards in instance tables),
- instance paths unique per table,
- non-empty technical category on data rows,
- no removed types (`Technical Knowledge`), no non-structural types
  (`Technical Activity`), no legacy `... Technique Type` suffix names,
- no category segments inside type paths,
- the root is never re-expressed through an intermediate node (no type
  segment directly beneath the root repeats the root's own type, save
  the documented allowlist),
- no type segment terminates a branch.

Instance-path styling (`**bold**` intermediates, `` `code` `` types) is
normalized away before structural checks.

Usage: python3 src/note/bin/conform.py [file ...]
Default: all technical notes carrying decomposition tables.
Exit 1 on any violation. Stdlib only.
"""

import re
import sys
from pathlib import Path

NOTE = Path(__file__).resolve().parent.parent
PHILOSOPHIA = NOTE / "app/notes/general/philosophia-artium-technicarum-et-operis.md"

DEFAULT_FILES = [
    NOTE / "app/notes/cto/es/multinode/openapi.md",
    NOTE / "app/notes/cto/es/multinode/java-ee-jakarta-ee.md",
    NOTE / "app/notes/cto/es/multinode/jobrunr.md",
    NOTE / "app/notes/cto/es/multinode/marketing-technical-practice.md",
    NOTE / "app/notes/cto/es/multinode/wildfly.md",
    NOTE / "app/notes/cto/es/multinode/biotechnology.md",
    NOTE / "app/notes/pto/eclipse.md",
]

GRAMMAR_ROW_RE = re.compile(r"^\|\s*`(\(root\)[^`]*)`")
BACKTICK_RE = re.compile(r"`([^`]*)`")
CATEGORIES = {
    "Composite", "Technical Context", "Requirements & Definition",
    "Knowledge & Methodology", "Agents & Competence", "System Structure",
    "System Relations", "Mechanism & Capability", "Technique",
    "Technical Control", "Lifecycle & Continuity",
}

# Types removed from (or never part of) the grammar with a fixed verdict.
REMOVED = {"Technical Knowledge": "removed type (see philosophia QA)"}
NON_STRUCTURAL = {"Technical Activity": "operation, not structure (see philosophia QA)"}
LEGACY_SUFFIX_RE = re.compile(
    r"^(General|Operative|Constitutive) Technique Type$"
)

# Sanctioned exception to the root-repetition rule (see philosophia
# No-repetition rule): a same-type segment scoping a genuine instance
# family — currently only Biotechnology's control set.
ROOT_REPEAT_ALLOWLIST = {"Biotechnology > Technical Element Set"}


def load_grammar():
    """Return (grammar_paths, canonical) from the philosophia Recursive view.

    canonical maps a terminal type name to its full grammar path.
    """
    text = PHILOSOPHIA.read_text()
    section = text.split("### Recursive view")[1].split(
        "## How to decompose")[0]
    grammar = set()
    for line in section.splitlines():
        m = GRAMMAR_ROW_RE.match(line)
        if m:
            grammar.add(m.group(1))
    canonical = {}
    for path in grammar:
        if "..." in path or "{" in path:
            continue
        terminal = path.split(" > ")[-1]
        canonical.setdefault(terminal, path)
    return grammar, canonical


def table_rows(lines):
    """Yield (lineno, cells) for rows of Instance-Tree-Path tables."""
    in_table = False
    for i, line in enumerate(lines, 1):
        if line.startswith("|") and "Technical Element Type Tree Path" in line:
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and set(cells) != {"---"} and \
                    cells[0] != "Instance Tree Path" and \
                    any(cells[:4]):
                yield i, cells


def check_file(path, grammar, canonical):
    errors = []
    typenames = set(canonical)

    def norm(inst):
        # Strip bold root markers (presentational, not part of the path)
        # and backticks only around known type names; backticked code
        # names in instance cells (e.g. `beans.xml`) stay literal.
        inst = re.sub(r"\*\*(.+?)\*\*", r"\1", inst)
        return re.sub(
            r"`([^`]*)`",
            lambda m: m.group(1).strip()
            if m.group(1).strip() in typenames else m.group(0),
            inst)
    lines = Path(path).read_text().splitlines()
    seen = {}
    rows = [(lineno, cells) for lineno, cells in table_rows(lines)]
    for lineno, cells in rows:
        inst = norm(cells[0])
        typecell = cells[3]
        if inst in seen:
            errors.append(
                f"{lineno}: duplicate instance path '{inst}' "
                f"(first at {seen[inst]})")
        else:
            seen[inst] = lineno
        if not cells[2]:
            errors.append(f"{lineno}: empty technical category")
            continue
        m = BACKTICK_RE.search(typecell)
        tpath = m.group(1).strip() if m else typecell.strip()
        if not tpath:
            errors.append(f"{lineno}: empty type path")
            continue
        if "..." in tpath or "{" in tpath:
            errors.append(f"{lineno}: wildcard in instance table: `{tpath}`")
            continue
        terminal = tpath.split(">")[-1].strip()
        if terminal in REMOVED:
            errors.append(
                f"{lineno}: {REMOVED[terminal]}: `{tpath}`")
            continue
        if terminal in NON_STRUCTURAL:
            errors.append(
                f"{lineno}: {NON_STRUCTURAL[terminal]}: `{tpath}`")
            continue
        if LEGACY_SUFFIX_RE.match(terminal):
            errors.append(
                f"{lineno}: legacy suffix name "
                f"(use '{terminal[:-5]}'): `{tpath}`")
            continue
        if any(seg.strip() in CATEGORIES
               for seg in tpath.split(">")[:-1]):
            errors.append(f"{lineno}: category segment in path: `{tpath}`")
            continue
        if tpath not in grammar:
            if terminal in canonical:
                errors.append(
                    f"{lineno}: non-canonical path `{tpath}` "
                    f"(canonical: `{canonical[terminal]}`)")
            else:
                errors.append(
                    f"{lineno}: unknown terminal type "
                    f"'{terminal}': `{tpath}`")
    # The root must not be re-expressed through an intermediate node:
    # no type segment directly beneath the root row may repeat the
    # root's own type as bare re-expression (allowlist documents the
    # sanctioned scoping exception). Deeper same-type nesting is
    # legitimate recursion and stays allowed.
    by_path = {}
    for lineno, cells in rows:
        by_path[norm(cells[0])] = (lineno, cells)
    roots = [p for p in by_path if ">" not in p]
    for root in roots:
        rm = BACKTICK_RE.search(by_path[root][1][3])
        rterm = (rm.group(1).strip() if rm
                 else by_path[root][1][3].strip()).split(">")[-1].strip()
        for lineno, cells in rows:
            segs = [s.strip() for s in norm(cells[0]).split(">")]
            if len(segs) == 2 and segs[0] == root and segs[1] in typenames \
                    and segs[1] == rterm and \
                    norm(cells[0]) not in ROOT_REPEAT_ALLOWLIST:
                errors.append(
                    f"{lineno}: segment `{segs[1]}` repeats the root "
                    f"row's own type")
    # No type segment may terminate a branch: a row that claims to BE a
    # type (terminal segment equals its own fourth-column terminal) must
    # be extended by another row. Plain instances that merely share a
    # type's name (e.g. a `Validation` feature typed as a Mechanism)
    # are unaffected.
    for lineno, cells in rows:
        full = norm(cells[0])
        term = full.split(">")[-1].strip()
        if term not in typenames:
            continue
        m = BACKTICK_RE.search(cells[3])
        own = (m.group(1).strip() if m
               else cells[3].strip()).split(">")[-1].strip()
        if own == term and not any(
                q != full and q.startswith(full + " > ")
                for q in by_path):
            errors.append(
                f"{lineno}: type segment `{term}` terminates a branch")
    return errors


def main(files):
    grammar, canonical = load_grammar()
    total = 0
    for f in files:
        errors = check_file(f, grammar, canonical)
        try:
            rel = Path(f).relative_to(NOTE.parent.parent)
        except ValueError:
            rel = Path(f)
        if errors:
            print(f"{rel}: {len(errors)} violation(s)")
            for e in errors:
                print(f"  {e}")
            total += len(errors)
        else:
            print(f"{rel}: OK")
    print(f"total violations: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    files = sys.argv[1:] or [str(f) for f in DEFAULT_FILES]
    sys.exit(main(files))
