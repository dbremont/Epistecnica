# Courses

> The courses corpus behind Epistecnica — one directory per course, one
> entry plus a set of lectures — indexed and served at `/course/`.

## Layout

```
src/course/
├── README.md        # this document
├── bin/index.py     # search-index builder (stdlib only)
└── app/             # served statically at /course/
    ├── index.html   # catalog: search + kind + tag facets
    ├── course.html  # course view (?c=<dir>): entry plus its lectures
    ├── lecture.html # lecture view (?l=<dir>/<file>)
    ├── courses.css  # markdown typography (shared design tokens)
    ├── data/        # generated (index.json — do not edit)
    └── courses/     # the corpus (never machine-edited)
        └── <course-dir>/
            ├── readme.md        # the entry (title, overview, lecture list)
            ├── 01-*.md          # lecture files, sort order = read order
            └── 02-*.md
```

- Regenerate the search index after any corpus change: `make course-index`.
- A **course** is a directory: `readme.md` is the entry (title from its
  first `# ` heading), every other `*.md` is a lecture. The course view
  renders the entry, then lists that course's lectures (from the index)
  linking to their lecture pages — the entry-plus-lectures shape is what
  makes a course a course in the view.
- The index holds two kinds: `course` (path `<dir>`) and `lecture`
  (path `<dir>/<file>`, with a `course` parent field). The catalog
  facets by kind (`all`, `course`, `lecture`) instead of sections.
- Optional `tags: [...]` front matter (`---`-fenced, same style as the
  glossarium aliases) types entries and lectures independently; tags
  surface as catalog facets and viewer chips, and rank between headings
  and body text in search. See `src/note/README.md` for the shared tag
  convention.
- Markdown rendering uses the notes vendor bundle relatively
  (`../note/vendor/marked.min.js`) — no duplicated runtime deps.

## Import

One-off migration from the Notion "Histórico de Cursos" export:

```
python3 src/course/bin/import.py <notion-export-dir>
python3 src/course/bin/index.py
```

The importer strips Notion uuid suffixes and writes one directory per
course file (`courses/<slug>/readme.md`, entry-only — the export holds
whole-course single pages, so no lecture structure is fabricated). The
Notion `Tags:` line becomes `tags:` front matter; bare `: <number>`
property lines, ellipsis-only (`> …`) placeholders, and empty
`## Index` headings are dropped; referenced images are copied into the
course directory with rewritten qualified links. Existing course
directories are never touched (colliding slugs are skipped with a
warning). Afterwards the corpus under `app/courses/` is the source of
truth — edit entries by hand and rerun `make course-index`.

## Naming convention

Same rules as the notes corpus (see `src/note/README.md`): ASCII only,
lowercase, kebab-case — for course directories, `.md` filenames
(`readme.md` fixed for the entry), and tags.

`bin/index.py` warns (never fails) on a misnamed course directory, a
course missing `readme.md`, or any bad lecture/tag name. Keep the output
warning-free.
