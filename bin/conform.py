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
]

HEADER = "| Instance Tree Path | Description |"
TYPE_ROW = re.compile(r"^\|\s*`[^`]*\(→[^)]*\)\s*([^`]+)`")

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
    block = []
    for i, line in enumerate(lines, 1):
        if line.strip() == HEADER:
            if block:
                yield block
            block = []
            continue
        if line.startswith("|") and block:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 2 and set(cells) != {"---"}:
                block.append((i, cells))
        elif not line.startswith("|"):
            if block:
                yield block
                block = []
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
            segs = [s.strip() for s in full.split(" → ")]
            if not full or any(not s for s in segs):
                errors.append(f"{lineno}: empty segment in path")
                continue
            for i, seg in enumerate(segs):
                if not (seg.startswith("`") and seg.endswith("`")):
                    continue
                name = seg[1:-1].strip()
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
                if i == len(segs) - 1:
                    errors.append(
                        f"{lineno}: type segment `{name}` terminates a branch")
                grouping_paths.add(" → ".join(segs[:i + 1]))
            if full in seen:
                errors.append(
                    f"{lineno}: duplicate instance path '{full}' "
                    f"(first at {seen[full]})")
            seen.setdefault(full, lineno)
            paths.add(full)
        for gp in grouping_paths:
            if not any(p.startswith(gp + " → ") for p in paths):
                errors.append(f"type segment with no children: '{gp}'")
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
