# Courses

> The courses corpus behind Epistecnica — one directory per course, one
> entry plus a set of lectures — indexed and served at `/corpus/courses`.

## Layout

```
src/corpus/
├── README-courses.md    # this document
├── app/                 # shared catalog + global viewer + generated data
│   ├── index.html
│   ├── note.html        # global markdown viewer (?p=courses/<dir>/readme.md)
│   ├── corpus.css
│   └── data/            # generated indexes, changelogs
└── courses/             # the courses corpus (served at /corpus/courses)
    ├── atlas.html       # the atlas of courses (a live page)
    └── <course-dir>/
        ├── readme.md    # the entry (title, overview, lecture list)
        ├── 01-*.md      # lectures, sort order = read order
        └── 02-*.md
```

- Regenerate the search index after any corpus change: `make course-index`.
- **Live HTML pages**: any standalone `*.html` anywhere in the corpus (not a
  course dir) is indexed as an ordinary entry with kind `live` — title from
  `<title>`, else the first `<h1>` — and the catalog renders it as a card
  with a `live` badge linking straight to the served page (the universal
  search and the universal view route it the same way).
- **The atlas** (`courses/atlas.html`, served at
  `/corpus/coursesatlas.html`, a live page listed in the catalog and
  linked from the catalog footer and the hub footer) maps the two source
  course lists —
  [courses.md](https://gist.github.com/dbremont/914cdbcf861238742ea1d41c7bf0d08e)
  and
  [science-courses.md](https://gist.github.com/dbremont/fd5a44f3d064ad23ac8e3612f828e216)
  — against the corpus, one **field** section per source section. One row per
  course: the primary link opens the corpus course page when a directory
  exists (badge `in corpus`), otherwise the source link; every other
  occurrence of the same course (another offering, year, or source) rides
  along on that row as **references**. The seven anchor courses carry the
  `main` badge. Same course number with a different title (14.451, 14.452,
  9.98, 18.S096) means a different course — both rows stay, noted in place.
  The page is static HTML (a client-side filter and the shared nav search
  are its only scripts); edit its rows by hand and keep the source links
  intact.
- A **course** is a directory: `readme.md` is the entry (title from its
  first `# ` heading), every other `*.md` is a lecture. The course view
  renders the entry, then lists that course's lectures (from the index)
  linking to their lecture pages — the entry-plus-lectures shape is what
  makes a course a course in the view.
- The index holds two kinds: `course` (path `<dir>`) and `lecture`
  (path `<dir>/<file>`, with a `course` parent field). The catalog follows
  the Naturgnosis model (see `src/corpus/README-notes.md` §Catalog): `browse` lists
  one folder card per course, and entering a folder shows the course entry
  (`note.html?p=courses/<dir>/readme.md`) plus its lecture cards
  (`note.html?p=courses/<dir>/<file>`); `files` flattens the corpus. There are no
  facet bars — kind is a badge on each card, tags are `@tag` search tokens.
- Optional `tags: [...]` front matter (`---`-fenced, the same
  front-matter style used across the corpora) types entries and lectures
  independently; tags surface as `@tag` search tokens and viewer chips
  (`?q=@<tag>` deep links), and rank between headings and body text in
  search. See `src/corpus/README-notes.md` for the shared tag convention.
- The same front matter may carry a `qa:` block list of open reflection
  questions (one per `- ` line); a non-empty list shows a `QA · N` chip in
  the course and lecture viewers that opens the question list. See
  `src/corpus/README-notes.md` §QA questions.
- Markdown rendering uses the notes vendor bundle relatively
  (`../corpus/notesvendor/marked.min.js`) — no duplicated runtime deps.

## Changelog / history

Every markdown course entry and lecture carries a per-file edit history in
`app/data/changelog.json` (with `changelog.schema.json`): an array of
`{file_path, logs[]}` objects, `file_path` relative to `app/corpus/courses` (the
course entry is `<dir>/readme.md`). Each log is
`{date, summary; optional kind, commit, before}` — object key order follows
the schema. The existing history was backfilled from git by
`bin/backfill_changelog.py --corpus course`; new change sets append one log
per touched entry or lecture in the same commit, then
`bin/link_changelog_commits.py --corpus course` stamps the commit shas in a
json-only annotation commit. The viewer's `history` chip opens the modal.
Only content changes are logged: metadata-only front-matter edits (`tags:`,
`qa:`) append no log. See `src/corpus/README-notes.md` §Changelog / history for the
full contract.

## Import

One-off migration from the Notion "Histórico de Cursos" export:

```
python3 bin/course_import.py <notion-export-dir>
python3 bin/course_index.py
```

The importer strips Notion uuid suffixes and writes one directory per
course file (`courses/<slug>/readme.md`, entry-only — the export holds
whole-course single pages, so no lecture structure is fabricated). The
Notion `Tags:` line becomes `tags:` front matter; bare `: <number>`
property lines, ellipsis-only (`> …`) placeholders, and empty
`## Index` headings are dropped; referenced images are copied into the
course directory with rewritten qualified links. Existing course
directories are never touched (colliding slugs are skipped with a
warning). Afterwards the corpus under `app/corpus/courses` is the source of
truth — edit entries by hand and rerun `make course-index`.

## Naming convention

Same rules as the notes corpus (see `src/corpus/README-notes.md`): ASCII only,
lowercase, kebab-case — for course directories, `.md` filenames
(`readme.md` fixed for the entry), and tags.

`bin/course_index.py` warns (never fails) on a misnamed course directory, a
course missing `readme.md`, or any bad lecture/tag name. Keep the output
warning-free.

Every course and lecture file carries `course` as its **first** tag, so the
top-level corpus is visible in search and in the viewer:

```markdown
---
tags: [course, algorithms, computation]
---
```

`bin/check_corpus_tags.py` (part of `make check`) enforces this.
