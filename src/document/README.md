# Documents

> The documents corpus behind Epistecnica — papers, articles, books as
> plain-markdown entries with summary, formulation, and references —
> indexed and served at `/document/`.

## Layout

```
src/document/
├── README.md        # this document
├── bin/index.py     # search-index builder (stdlib only)
└── app/             # served statically at /document/
    ├── index.html   # catalog: search + section + tag facets
    ├── document.html# single-document viewer (?d=<path>)
    ├── documents.css# markdown typography (shared design tokens)
    ├── data/        # generated (index.json — do not edit)
    └── documents/   # the corpus (never machine-edited)
        ├── papers/  # one .md per paper
        ├── articles/# one .md per article
        └── books/   # one .md per book
```

- Regenerate the search index after any corpus change: `make document-index`.
- Documents are plain markdown entries: title comes from the first `# `
  heading (else the filename); the top-level directory is the section
  (`papers`, `articles`, `books`, …).
- Optional `tags: [...]` front matter (`---`-fenced, same style as the
  glossarium aliases) types each document; tags surface as catalog facets
  and viewer chips, and rank between headings and body text in search.
  See `src/note/README.md` for the shared tag convention.
- Markdown rendering uses the notes vendor bundle relatively
  (`../note/vendor/marked.min.js`) — no duplicated runtime deps.

## Import

One-off migration from the Notion "Catalogus Documentorum" export:

```
python3 src/document/bin/import.py <notion-export-dir>
python3 src/document/bin/index.py
```

The importer strips Notion uuid suffixes, classifies by bibtex entry
type (`@book`/`@inbook` → books, `@article` → articles, everything else
→ papers; placeholder-only files fall back to venue heuristics and
default to articles, printed as a review list), converts the Notion
`Tags:` line to `tags:` front matter (normalized; the `Unread` marker
dropped), copies referenced images beside their document into
`<section>/<slug>/` with rewritten section-qualified links, and never
overwrites existing files (colliding slugs get a numeric suffix).
Afterwards the corpus under `app/documents/` is the source of truth —
edit entries by hand and rerun `make document-index`.

## Naming convention

Same rules as the notes corpus (see `src/note/README.md`): ASCII only,
lowercase, kebab-case — for directories, `.md` filenames, and tags.

`bin/index.py` validates every document path and tag and prints warnings
for violations; warnings never fail the build. Keep the output
warning-free.
