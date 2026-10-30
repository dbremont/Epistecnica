#!/usr/bin/env python3
"""Decomposition-table conformance checker.

Verifies that every `Instance Tree Path` table in the technical notes
follows the canonical table form owned by the technica guide, fetched at
runtime from Naturgnosis:

    | Instance Tree Path | Description |

- paths split on `→`, a unique, complete path from the root per row;
- backticked segments are type groupings and must name a guide type
  (the Tabular view's `(→ Link) Type` rows);
- plain segments are instances; a path never ends in a type segment;
- instance paths are unique within a table;
- no removed / non-structural / legacy-suffix type names.

Usage: python3 bin/conform.py [file ...]
Default: all technical notes carrying decomposition tables.
Exit 1 on any violation, 2 if the guide cannot be fetched. Stdlib only.
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "src" / "note"
GRAMMAR_URL = (
    "https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/"
    "app/note/data/meta/philosophia-artium-technicarum-et-operis.md"
)

DEFAULT_FILES = [
    NOTE / "app/data/technica/general/cto/es/multinode/openapi.md",
    NOTE / "app/data/technica/general/cto/es/multinode/java-ee-jakarta-ee.md",
    NOTE / "app/data/technica/general/cto/es/multinode/jobrunr.md",
    NOTE / "app/data/technica/general/cto/es/multinode/wildfly.md",
    NOTE / "app/data/technica/general/cto/es/multinode/biotechnology.md",
    NOTE / "app/data/technica/general/pto/eclipse.md",
    NOTE / "app/data/technica/general/cto/es/multinode/energy-technology.md",
    NOTE / "app/data/technica/general/cto/es/multinode/physical-material-technology.md",
    NOTE / "app/data/technica/computation/representation.md",
]

HEADER = "| Instance Tree Path | Description |"
TYPE_ROW = re.compile(r"^\|\s*`[^`]*\(→[^)]*\)\s*([^`]+)`")

# The relationship types the guide licenses for labelling a link
# ("Which relationship types can be used to explicitly label the → operator?").
REL_TYPES = {
    "Kind", "Part", "Has", "Instance", "Depends", "Interacts", "Produces",
    "Enables", "Transforms", "Uses", "Acts On", "Implements",
    "Constrained By", "Governed By", "Evaluated By", "Maintained By",
    "Evolves Through", "Unspecified",
}

TOKEN = re.compile(r"`([^`]*)`|([^`]+)")
LINK = re.compile(r"^\(\s*(?:→|->)\s*(.+?)\s*\)$")
LINKED = re.compile(r"`\(\s*(?:→|->)")


def parse_path(cell):
    """[(name, kind, link)] for one path cell, in either accepted grammar.

    Old form: `A` → B → `C` — links are bare, typing by backticks.
    New form: `A` `(→ Kind)` `B` `(→ Instance)` C — every link is labelled;
    the path starts at the root node `Technical Element`.

    `kind` is root|grouping|instance; `link` is the relationship type
    preceding the node, or None.
    """
    cell = cell.strip()
    if not cell:
        return []
    if LINKED.search(cell):
        segs, link = [], None
        for match in TOKEN.finditer(cell):
            code, plain = match.group(1), match.group(2)
            if code is not None:
                inner = code.strip()
                label = LINK.match(inner)
                if label:
                    link = label.group(1).strip()
                else:
                    segs.append((inner, "grouping", link))
                    link = None
            else:
                text = plain.strip()
                if not text:
                    continue
                segs.append((text, "instance", link))
                link = None
        if segs and segs[0][0] == "Technical Element" and segs[0][2] is None:
            segs[0] = ("Technical Element", "root", None)
        return segs
    segs = []
    for raw in cell.split(" → "):
        raw = raw.strip()
        if not raw:
            return []
        if raw.startswith("`") and raw.endswith("`"):
            segs.append((raw[1:-1].strip(), "grouping", None))
        else:
            segs.append((raw, "instance", None))
    return segs


REMOVED = {"Technical Knowledge": "removed type (see philosophia QA)"}
NON_STRUCTURAL = {"Technical Activity": "operation, not structure (see philosophia QA)"}
LEGACY_SUFFIX = re.compile(r"^(General|Operative|Constitutive) Technique Type$")


def fetch_guide(url=GRAMMAR_URL):
    """Fetch the canonical technica guide text at runtime (no local copy)."""
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return resp.read().decode("utf-8")
    except (urllib.error.URLError, OSError) as exc:
        print(f"ERROR: cannot fetch the technica guide ({url}): {exc}",
              file=sys.stderr)
        raise SystemExit(2)


def load_types(text):
    """Type names from the guide's Tabular view rows."""
    types = set()
    for line in text.splitlines():
        m = TYPE_ROW.match(line)
        if m:
            types.add(m.group(1).strip())
    return types


def tables(lines):
    """Yield (start_lineno, [(lineno, cells), ...]) per decomposition table."""
    block = None
    for i, line in enumerate(lines, 1):
        if line.strip() == HEADER:
            if block:
                yield block
            block = []
            continue
        if block is None:
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 2 and set(cells) != {"---"}:
                block.append((i, cells))
        else:
            if block:
                yield block
            block = None
    if block:
        yield block


def check_file(path, types):
    errors = []
    lines = Path(path).read_text().splitlines()
    for block in tables(lines):
        seen = {}
        grouping_paths = set()
        paths = set()
        for lineno, cells in block:
            full = cells[0]
            segs = parse_path(full)
            if not segs:
                errors.append(f"{lineno}: empty segment in path")
                continue
            labelled = segs[0][2] is None and segs[0][1] == "root"
            key = tuple(s[0] for s in segs)
            for i, (name, kind, link) in enumerate(segs):
                if kind == "root":
                    continue
                if labelled:
                    if link is None:
                        errors.append(
                            f"{lineno}: bare arrow before '{name}' — every "
                            f"link must name its relationship type")
                    elif link not in REL_TYPES:
                        errors.append(
                            f"{lineno}: unknown relationship type "
                            f"`(→ {link})` (see the guide's relationship "
                            f"table in QA)")
                if kind != "grouping":
                    continue
                if name not in types:
                    errors.append(
                        f"{lineno}: unknown type segment `{name}`")
                if name in REMOVED:
                    errors.append(f"{lineno}: {REMOVED[name]}: `{name}`")
                if name in NON_STRUCTURAL:
                    errors.append(
                        f"{lineno}: {NON_STRUCTURAL[name]}: `{name}`")
                if LEGACY_SUFFIX.match(name):
                    errors.append(
                        f"{lineno}: legacy suffix name "
                        f"(use '{name[:-5]}'): `{name}`")
                grouping_paths.add(key[:i + 1])
            if key in seen:
                errors.append(
                    f"{lineno}: duplicate instance path '{full}' "
                    f"(first at {seen[key]})")
            seen.setdefault(key, lineno)
            paths.add(key)
        for gp in grouping_paths:
            if not any(p[:len(gp)] == gp and len(p) > len(gp) for p in paths):
                errors.append(
                    f"type segment with no children: '{' → '.join(gp)}'")
    return errors


def main(argv):
    files = [Path(a) for a in argv] or DEFAULT_FILES
    types = load_types(fetch_guide())
    if not types:
        print("ERROR: no types parsed from the technica guide",
              file=sys.stderr)
        return 2
    total = 0
    for path in files:
        errors = check_file(path, types)
        total += len(errors)
        for err in errors:
            print(f"{path}: {err}", file=sys.stderr)
    if total:
        print(f"[conform] FAIL: {total} problem(s) in {len(files)} note(s)",
              file=sys.stderr)
        return 1
    print(f"[conform] ok: {len(files)} notes, canonical two-column tables, "
          f"{len(types)} guide types")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
