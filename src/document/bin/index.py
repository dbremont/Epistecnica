#!/usr/bin/env python3
"""
Documents index builder.

Scans src/document/app/documents/** for documents — markdown (*.md,
kind "document": papers, articles, books) — and emits
src/document/app/data/index.json, the search corpus for the documents
catalog (/document/). Stdlib only.

For each document it extracts: path (relative to documents/), title
(first "# " heading; fallback: the filename), top-level section (first
path component: papers, articles, books, …), h2/h3 headings, tags
(optional `tags: [...]` front matter, same `---` style as the
glossarium aliases), lowercased plain text, and word count. Paths and
tags are validated against the naming convention (see
src/document/README.md); violations print as warnings and never fail
the build.

Usage: python3 src/document/bin/index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

DOCUMENT = Path(__file__).resolve().parent.parent
APP = DOCUMENT / "app"
DOCUMENTS = APP / "documents"
OUT = APP / "data" / "index.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
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


def parse_tags(md: str, rel: Path, warnings: list) -> tuple:
    """Split optional `---` front matter off; return (body, tags).

    Only the `tags: [...]` line is read; anything else in the fence is
    ignored. Invalid tags warn and are dropped.
    """
    tags = []
    fm = FRONT_MATTER_RE.match(md)
    if fm:
        for line in fm.group(1).splitlines():
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
    return md, tags


def parse(path: Path, rel: Path, warnings: list) -> dict:
    md = path.read_text(encoding="utf-8", errors="replace")
    md, tags = parse_tags(md, rel, warnings)
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
    return entry(rel, title, headings, text, tags, kind="document")


def entry(rel: Path, title: str, headings: list, text: str, tags: list, kind: str) -> dict:
    parts = rel.parts
    section = parts[0] if len(parts) > 1 else "root"
    return {
        "path": rel.as_posix(),
        "title": title,
        "section": section,
        "kind": kind,
        "tags": tags,
        "headings": headings,
        "text": text,
        "words": len(text.split()),
    }


def main() -> int:
    if not DOCUMENTS.is_dir():
        print(f"ERROR: documents directory not found: {DOCUMENTS}", file=sys.stderr)
        return 1

    warnings: list = []
    documents: list = []
    for path in sorted(DOCUMENTS.rglob("*.md")):
        rel = path.relative_to(DOCUMENTS)
        check_name(rel, warnings)
        documents.append(parse(path, rel, warnings))

    sections: dict = {}
    for n in documents:
        sections[n["section"]] = sections.get(n["section"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(documents),
        "sections": sections,
        "documents": documents,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    tagged = sum(1 for n in documents if n["tags"])
    print(f"documents-index: {len(documents)} documents ({tagged} tagged), {sum(n['words'] for n in documents)} words -> {OUT.relative_to(DOCUMENT.parent.parent)} ({kb:.0f} KB)")
    for section, count in sorted(sections.items()):
        print(f"  {section}: {count}")
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/document/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
