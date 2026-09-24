#!/usr/bin/env python3
"""
Courses index builder.

Scans src/course/app/courses/*/ for courses — one directory per course
with a readme.md entry plus lecture *.md files — and emits
src/course/app/data/index.json, the search corpus for the courses
catalog (/course/). Stdlib only.

For each course it emits one entry (kind "course", path "<dir>") and one
entry per lecture (kind "lecture", path "<dir>/<file>", with a "course"
parent field). Each entry extracts: title (first "# " heading;
fallback: the filename), h2/h3 headings, tags (optional `tags: [...]`
front matter, same `---` style as the glossarium aliases), lowercased
plain text, and word count. Paths and tags are validated against the
naming convention (see src/course/README.md); violations print as
warnings and never fail the build.

Usage: python3 src/course/bin/index.py
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

COURSE = Path(__file__).resolve().parent.parent
APP = COURSE / "app"
COURSES = APP / "courses"
OUT = APP / "data" / "index.json"

ENTRY_FILE = "readme.md"

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
    return entry(rel, title, headings, text, tags, kind="lecture")


def entry(rel: Path, title: str, headings: list, text: str, tags: list, kind: str, course: str = None) -> dict:
    item = {
        "path": rel.as_posix(),
        "title": title,
        "kind": kind,
        "tags": tags,
        "headings": headings,
        "text": text,
        "words": len(text.split()),
    }
    if course is not None:
        item["course"] = course
    return item


def main() -> int:
    if not COURSES.is_dir():
        print(f"ERROR: courses directory not found: {COURSES}", file=sys.stderr)
        return 1

    warnings: list = []
    entries: list = []
    for course_dir in sorted(p for p in COURSES.iterdir() if p.is_dir()):
        if not NAME_RE.match(course_dir.name):
            warnings.append(f"{course_dir.name} (course directory)")
            continue
        entry_file = course_dir / ENTRY_FILE
        if not entry_file.is_file():
            warnings.append(f"{course_dir.name} (missing {ENTRY_FILE})")
            continue
        rel = Path(course_dir.name)
        check_name(rel / ENTRY_FILE, warnings)
        course = parse(entry_file, rel, warnings)
        course["path"] = course_dir.name
        course["kind"] = "course"
        entries.append(course)
        for path in sorted(course_dir.glob("*.md")):
            if path.name == ENTRY_FILE:
                continue
            lecture_rel = Path(course_dir.name) / path.name
            check_name(lecture_rel, warnings)
            lecture = parse(path, lecture_rel, warnings)
            lecture["course"] = course_dir.name
            entries.append(lecture)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(entries),
        "courses": sum(1 for n in entries if n["kind"] == "course"),
        "lectures": sum(1 for n in entries if n["kind"] == "lecture"),
        "entries": entries,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    kb = OUT.stat().st_size / 1024
    tagged = sum(1 for n in entries if n["tags"])
    print(f"courses-index: {payload['courses']} courses, {payload['lectures']} lectures ({tagged} tagged), {sum(n['words'] for n in entries)} words -> {OUT.relative_to(COURSE.parent.parent)} ({kb:.0f} KB)")
    if warnings:
        print(f"naming warnings: {len(warnings)} (see src/course/README.md)")
        for w in warnings:
            print(f"  ! {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
