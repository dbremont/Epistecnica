# Documents

> The documents corpus behind Epistecnica — papers, articles, books as
> plain-markdown entries with summary, formulation, and references —
> indexed and served at `/corpus/documents`.

## Layout

```
src/corpus/
├── README-documents.md  # this document
├── app/                 # shared catalog + global viewer + generated data
│   ├── /explorer.html
│   ├── view.html        # global markdown viewer (?p=documents/<path>)
│   ├── corpus.css
│   └── data/            # generated indexes, changelogs
└── documents/           # the documents corpus (served at /corpus/documents)
    ├── papers/          # one .md per paper
    ├── articles/        # one .md per article
    └── books/           # one .md per book
```

- Regenerate the search index after any corpus change: `make document-index`.
- Documents are plain markdown entries: title comes from the first `# `
  heading (else the filename); the top-level directory is the section
  (`papers`, `articles`, `books`, …). The catalog follows the Naturgnosis
  model (see `src/corpus/README-notes.md` §Catalog): `browse` lists one folder card
  per section, and entering a folder shows its document cards; `files`
  flattens the corpus. There are no facet bars — tags are `@tag` search
  tokens.
- Optional `tags: [...]` front matter (`---`-fenced, the same
  front-matter style used across the corpora) types each document; tags
  surface as `@tag` search tokens and viewer chips (`?q=@<tag>` deep
  links), and rank between headings and body text in search.
  See `src/corpus/README-notes.md` for the shared tag convention.
- The same front matter may carry a `qa:` block list of open reflection
  questions (one per `- ` line); a non-empty list shows a `QA · N` chip in
  the viewer that opens the question list. See `src/corpus/README-notes.md` §QA
  questions.
- Markdown rendering uses the notes vendor bundle relatively
  (`../corpus/notesvendor/marked.min.js`) — no duplicated runtime deps.

## Changelog / history

Every markdown document carries a per-file edit history in
`app/data/changelog.json` (with `changelog.schema.json`): an array of
`{file_path, logs[]}` objects, `file_path` relative to `app/corpus/documents`.
Each log is `{date, summary; optional kind, commit, before}` — object key
order follows the schema. The existing history was backfilled from git by
`bin/backfill_changelog.py --corpus document`; new change sets append one
log per touched document in the same commit, then
`bin/link_changelog_commits.py --corpus document` stamps the commit shas in
a json-only annotation commit. The viewer's `history` chip opens the modal.
Only content changes are logged: metadata-only front-matter edits (`tags:`,
`qa:`) append no log. See `src/corpus/README-notes.md` §Changelog / history for the
full contract.

## Import

One-off migration from the Notion "Catalogus Documentorum" export:

```
python3 bin/document_import.py <notion-export-dir>
python3 bin/document_index.py
```

The importer strips Notion uuid suffixes, classifies by bibtex entry
type (`@book`/`@inbook` → books, `@article` → articles, everything else
→ papers; placeholder-only files fall back to venue heuristics and
default to articles, printed as a review list), converts the Notion
`Tags:` line to `tags:` front matter (normalized; the `Unread` marker
dropped), copies referenced images beside their document into
`<section>/<slug>/` with rewritten section-qualified links, and never
overwrites existing files (colliding slugs get a numeric suffix).
Afterwards the corpus under `app/corpus/documents` is the source of truth —
edit entries by hand and rerun `make document-index`.

## Naming convention

Same rules as the notes corpus (see `src/corpus/README-notes.md`): ASCII only,
lowercase, kebab-case — for directories, `.md` filenames, and tags.

`bin/document_index.py` validates every document path and tag and prints warnings
for violations; warnings never fail the build. Keep the output
warning-free.

Every document carries `document` as its **first** tag, so the top-level
corpus is visible in search and in the viewer:

```markdown
---
tags: [document, book, probability]
---
```

`bin/check_corpus_tags.py` (part of `make check`) enforces this.
