#!/usr/bin/env python3
"""
Notes index builder.

Scans src/note/app/data/** for notes — markdown (*.md, kind "note") and
self-contained HTML live notes (*.html, kind "live") — and emits
src/note/app/data/index.json, the search corpus for the notes catalog
(/note/). Stdlib only.

For each note it extracts: path (relative to data/), title (markdown:
first "# " heading; html: <title>, else first <h1>; fallback: the
filename), top-level section (first path component), h2/h3 headings,
tags (optional `tags: [...]` front matter, `---` style), order
(optional `order:` front-matter natural number — the note's render
position among the files of its directory), qa questions (optional `qa:`
block-list front matter), lowercased plain text, and word
count. Paths and tags are validated against the naming convention (see
src/note/README.md); violations print as warnings and never fail the
build.

Usage: python3 bin/notes_index.py
"""

import json
import re
import sys
from datetime import date
from html import unescape
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "src" / "note"
APP = NOTE / "app"
NOTES = APP / "data"
OUT = APP / "data" / "index.json"
LINKS = APP / "data" / "links.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TAGS_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$")
QA_KEY_RE = re.compile(r"^qa:\s*$")
QA_ITEM_RE = re.compile(r"^-\s+(.+)$")
ORDER_RE = re.compile(r"^order:\s*(\S+)\s*$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
FENCE_RE = re.compile(r"```[^\n]*\n|```")
HTML_BLOCK_RE = re.compile(r"<(script|style)\b.*?</\1>", re.IGNORECASE | re.DOTALL)
HTML_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
HTML_H_RE = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")


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
    """Split optional `---` front matter off; return (body, tags, qa, order).

    `tags: [...]`, a `qa:` block list (one open question per `- ` line), and
    `order:` (a natural number: the note's render position among the files of
    its directory) are read; anything else in the fence is ignored. Invalid
    tags and orders warn and are dropped.
    """
    tags = []
    qa = []
    order = None
    fm = FRONT_MATTER_RE.match(md)
    if fm:
        in_qa = False
        for line in fm.group(1).splitlines():
            stripped = line.strip()
            if in_qa:
                m = QA_ITEM_RE.match(stripped)
                if m:
                    question = m.group(1).strip().strip("'\"")
                    if question:
                        qa.append(question)
                    continue
                if not stripped:
                    continue
                in_qa = False
            if QA_KEY_RE.match(stripped):
                in_qa = True
                continue
            m = TAGS_RE.match(stripped)
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
                continue
            m = ORDER_RE.match(stripped)
            if m:
                raw = m.group(1).strip().strip("'\"")
                if raw.isdigit():
                    order = int(raw)
                else:
                    warnings.append(f"{rel.as_posix()} (order '{raw}')")
        md = md[fm.end():]
    return md, tags, qa, order


def parse(path: Path, rel: Path, warnings: list) -> dict:
    md = path.read_text(encoding="utf-8", errors="replace")
    md, tags, qa, order = parse_front_matter(md, rel, warnings)
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
    return entry(rel, title, headings, text, tags, qa, kind="note", order=order)


def parse_html(path: Path, rel: Path, warnings: list) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = HTML_BLOCK_RE.sub(" ", raw)

    title = None
    m = HTML_TITLE_RE.search(body)
    if m:
        title = HTML_TAG_RE.sub(" ", m.group(1)).strip()
    headings = []
    for hm in HTML_H_RE.finditer(body):
        level = int(hm.group(1))
        text = unescape(HTML_TAG_RE.sub(" ", hm.group(2))).strip()
        text = re.sub(r"\s+", " ", text)
        if not text:
            continue
        if level == 1 and title is None:
            title = text
        elif level >= 2:
            headings.append({"level": level, "text": text})
    if title is None:
        title = rel.stem.replace("-", " ")

    text = unescape(HTML_TAG_RE.sub(" ", body))
    text = re.sub(r"\s+", " ", text).strip().lower()
    return entry(rel, title, headings, text, [], [], kind="live")


def entry(rel: Path, title: str, headings: list, text: str, tags: list, qa: list, kind: str, order: int = None) -> dict:
    parts = rel.parts
    section = parts[0] if len(parts) > 1 else "root"
    item = {
        "path": rel.as_posix(),
        "title": title,
        "section": section,
        "kind": kind,
        "tags": tags,
    }
    if order is not None:
        item["order"] = order
    if qa:
        item["qa"] = qa
    item.update({
        "headings": headings,
        "text": text,
        "words": len(text.split()),
    })
    return item


def load_links(index_paths: set, warnings: list) -> list:
    """Read the links registry and return embedded {from, to, label, kind} pairs.

    The registry is the single fixed file data/links.json (a special file: never
    a note, never naming-validated). Each entry declares a directed support link;
    `from` is a directory node, `to` is a directory or a note. A dir `from` stays
    a directory node (embedded as {from: "<dir>/", ...}) — it is not expanded onto
    its descendants; a dir `to` stays a scope link. Unknown endpoints warn and are
    dropped, never failing the build.
    """
    if not LINKS.is_file():
        return []
    try:
        raw = json.loads(LINKS.read_text(encoding="utf-8"))
    except ValueError as exc:
        warnings.append(f"links.json (invalid JSON: {exc})")
        return []
    declared = raw.get("links", []) if isinstance(raw, dict) else []
    embedded = []
    for e in declared:
        if not isinstance(e, dict):
            warnings.append("links.json (entry is not an object)")
            continue
        frm = e.get("from", "") or ""
        to = e.get("to", "") or ""
        label = e.get("label", "") or ""
        kind = e.get("kind", "") or ""
        if frm.endswith("/"):
            if not (NOTES / frm).is_dir():
                warnings.append(f"links.json (unknown dir: {frm})")
                continue
            sources = [frm]
        elif frm in index_paths:
            sources = [frm]
        else:
            warnings.append(f"links.json (unknown note: {frm})")
            continue
        if to.endswith("/"):
            if not (NOTES / to).is_dir():
                warnings.append(f"links.json (unknown dir: {to})")
                continue
            targets = [to]
        elif to in index_paths:
            targets = [to]
        else:
            warnings.append(f"links.json (unknown note: {to})")
            continue
        for s in sources:
            for t in targets:
                embedded.append({"from": s, "to": t, "label": label, "kind": kind})
    return embedded


def main() -> int:
    if not NOTES.is_dir():
        print(f"ERROR: notes data directory not found: {NOTES}", file=sys.stderr)
        return 1

    warnings: list = []
    notes: list = []
    for pattern, parser in (("*.md", parse), ("*.html", parse_html)):
        for path in sorted(NOTES.rglob(pattern)):
            rel = path.relative_to(NOTES)
            check_name(rel, warnings)
            notes.append(parser(path, rel, warnings))

    sections: dict = {}
    for n in notes:
        sections[n["section"]] = sections.get(n["section"], 0) + 1

    links = load_links({n["path"] for n in notes}, warnings)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(notes),
        "sections": sections,
        "links": links,
        "notes": notes,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    tagged = sum(1 for n in notes if n["tags"])
    print(f"notes-index: {len(notes)} notes ({tagged} tagged), {len(links)} links, {sum(n['words'] for n in notes)} words -> {OUT.relative_to(NOTE.parent.parent)} ({kb:.0f} KB)")
    for section, count in sorted(sections.items()):
        print(f"  {section}: {count}")
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/note/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
