#!/usr/bin/env python3
"""
Personas index builder.

Scans src/persona/app/personas/ for persona entries — markdown (*.md,
kind "persona"), each carrying a `type:` front-matter field (e.g.
architecture, paper) — and emits src/persona/app/data/index.json, the
search corpus for the personas catalog (/persona/). Stdlib only.

For each entry it extracts: path (relative to personas/), title
(first "# " heading; fallback: the filename), type (the `type:`
front-matter value; missing or invalid types warn and fall back to
"untyped"), h2/h3 headings, tags (optional `tags: [...]` front matter,
same `---` style as the glossarium aliases), lowercased plain text,
and word count. Paths, types, and tags are validated against the
naming convention (see src/persona/README.md); violations print as
warnings and never fail the build.

Usage: python3 src/persona/bin/index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

PERSONA = Path(__file__).resolve().parent.parent
APP = PERSONA / "app"
PERSONAS = APP / "personas"
OUT = APP / "data" / "index.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TYPE_RE = re.compile(r"^type:\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*$")
TAGS_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
FENCE_RE = re.compile(r"```[^\n]*\n|```")


def check_name(rel: Path, warnings: list):
    for part in rel.parts[:-1]:
        if not NAME_RE.match(part):
            warnings.append(f"{rel.as_posix()} (directory '{part}')")
            return
    filename = rel.parts[-1]
    stem, dot, ext = filename.rpartition(".")
    if not NAME_RE.match(stem):
        warnings.append(f"{rel.as_posix()} (filename)")


def plain_text(md: str) -> str:
    md = FENCE_RE.sub("\n", md)
    md = LINK_RE.sub(r"\1", md)
    lines = []
    for line in md.splitlines():
        line = HEADING_RE.sub(r"\2", line)
        line = re.sub(r"[*_>`|]", " ", line)
        lines.append(line)
    return re.sub(r"\s+", " ", "\n".join(lines)).strip().lower()


def parse_front_matter(md: str, rel: Path, warnings: list) -> tuple:
    """Split optional `---` front matter off; return (body, type, tags).

    Only the `type:` and `tags: [...]` lines are read; anything else in
    the fence is ignored. A missing or invalid type warns and falls
    back to "untyped"; invalid tags warn and are dropped.
    """
    entry_type = None
    tags = []
    fm = FRONT_MATTER_RE.match(md)
    if fm:
        for line in fm.group(1).splitlines():
            tm = TYPE_RE.match(line.strip())
            if tm:
                candidate = tm.group(1).lower()
                if NAME_RE.match(candidate):
                    entry_type = candidate
                else:
                    warnings.append(f"{rel.as_posix()} (type '{candidate}')")
                continue
            m = TAGS_RE.match(line.strip())
            if m:
                for raw in m.group(1).split(","):
                    tag = raw.strip().strip("'\"").lower()
                    if not tag:
                        continue
                    if NAME_RE.match(tag):
                        if tag not in tags:
                            tags.append(tag)
                    else:
                        warnings.append(f"{rel.as_posix()} (tag '{tag}')")
        md = md[fm.end():]
    if entry_type is None:
        warnings.append(f"{rel.as_posix()} (missing type)")
        entry_type = "untyped"
    return md, entry_type, tags


def parse(path: Path, rel: Path, warnings: list) -> dict:
    md = path.read_text(encoding="utf-8", errors="replace")
    md, entry_type, tags = parse_front_matter(md, rel, warnings)
    title = None
    headings = []
    for line in md.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        level, text = len(m.group(1)), m.group(2).strip()
        if level == 1 and title is None:
            title = text
        elif level >= 2:
            headings.append({"level": level, "text": text})
    if title is None:
        title = rel.stem.replace("-", " ")
    text = plain_text(md)
    return entry(rel, title, headings, text, entry_type, tags, kind="persona")


def entry(rel: Path, title: str, headings: list, text: str, entry_type: str, tags: list, kind: str) -> dict:
    return {
        "path": rel.as_posix(),
        "title": title,
        "type": entry_type,
        "kind": kind,
        "tags": tags,
        "headings": headings,
        "text": text,
        "words": len(text.split()),
    }


def main() -> int:
    if not PERSONAS.is_dir():
        print(f"ERROR: personas directory not found: {PERSONAS}", file=sys.stderr)
        return 1

    warnings: list = []
    personas: list = []
    for path in sorted(PERSONAS.rglob("*.md")):
        rel = path.relative_to(PERSONAS)
        check_name(rel, warnings)
        personas.append(parse(path, rel, warnings))

    types: dict = {}
    for n in personas:
        types[n["type"]] = types.get(n["type"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(personas),
        "types": types,
        "personas": personas,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    tagged = sum(1 for n in personas if n["tags"])
    print(f"personas-index: {len(personas)} personas ({tagged} tagged), {sum(n['words'] for n in personas)} words -> {OUT.relative_to(PERSONA.parent.parent)} ({kb:.0f} KB)")
    for entry_type, count in sorted(types.items()):
        print(f"  {entry_type}: {count}")
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/persona/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
