# Glossarium

> The lexical corpus behind Epistecnica — terms and definitions, indexed
> and served at `/glossarium/`, with select-a-word lookup on the note pages.

## Layout

```
src/glossarium/
├── README.md        # this document
├── bin/
│   ├── import.py    # one-off Notion-export importer (stdlib only)
│   └── index.py     # search-index builder (stdlib only)
└── app/             # served statically at /glossarium/
    ├── index.html       # catalog: search + letter facets; ?t=<slug> = term view
    ├── glossarium.css   # markdown typography (shared design tokens)
    ├── js/              # selection-lookup popup (also wired into the note pages)
    ├── vendor/          # vendored runtime deps (marked.min.js)
    ├── data/        # generated (index.json — do not edit)
    └── terms/       # the corpus (one term per file; hand-edited after import)
```

- Regenerate the search index after any corpus change:
  `make glossarium-index` (runs `bin/index.py`).
- Terms are plain markdown: the name comes from the first `# ` heading.
  Optional `aliases: [ ... ]` front matter lists alternative spellings and
  translations used by the lookup; import writes it from the export CSV.

## Naming convention

Term slugs (the `<slug>.md` filenames) follow the same rules as the notes
corpus (see `src/note/README.md`): ASCII only, lowercase, kebab-case.
Original names keep their accents and case in the H1; slugs are
accent-folded (`Abstración` → `abstracion.md`).

## Import

One-off migration from the Notion "Glosarium" export:

```
python3 src/glossarium/bin/import.py <notion-export-dir>
python3 src/glossarium/bin/index.py
```

The importer strips Notion uuid suffixes and `: <n>` property noise, keeps
the markdown verbatim otherwise, and embeds CSV english translations as
aliases. Afterwards the corpus under `app/terms/` is the source of truth —
edit terms by hand and rerun `make glossarium-index`.

## Select-a-word lookup

`app/js/glossarium-lookup.js` is included by the notes catalog, the note
viewer, and the glossarium itself. It lazy-loads `data/index.json` on the
first text selection, matches the selection against names and aliases
(exact → alias → singular fallback), and shows a floating definition card
near the selection with a link to the full term. The index path is
injected per page via the script's `data-glossarium` attribute — always
relative (`../glossarium/data/index.json` from `/note/…` pages), keeping
the prefix-mount contract intact.
