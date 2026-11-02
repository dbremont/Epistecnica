# Glossarium

> The lexical corpus behind Epistecnica — terms and definitions, indexed and
> served at `/glossarium/`, with select-a-word lookup on the note pages.

## Layout

```
src/glossarium/
├── README.md        # this document
└── app/             # served statically at /glossarium/
    ├── index.html       # catalog (search, letter facets) + term view (?t=<slug>)
    ├── glossarium.css   # markdown typography (shared design tokens)
    ├── js/              # select-a-word popup (also wired into the notes pages)
    ├── vendor/          # vendored runtime deps (marked.min.js)
    └── data/
        ├── terms.json   # the corpus: source of truth (hand-maintained)
        └── index.json   # generated lookup/search index (do not edit)
```

- Terms are served from `data/terms.json` keyed by slug; there are no per-term
  markdown files. Add or replace one term with the importer, or edit the JSON.
- Regenerate the derived index after any corpus change: `make glossarium-index`
  (`bin/build_glossarium_index.py`, chunked and progress-aware — the server can
  also rebuild it through `POST /api/index/build`).
- `data/index.json` is generated and gitignored; the Dockerfile rebuilds it.

## Term shape

```json
{"slug": "technique", "name": "Technique", "aliases": ["tecnicidad"], "body": "# Technique\n…"}
```

- `slug` (the term code) is kebab-case: ASCII, lowercase, runs of
  non-alphanumerics folded to `-` (the same rule as note filenames).
- `name` is the term as displayed; `body` is markdown, whose first `# ` heading
  normally repeats the name.
- `aliases` lists alternative spellings and translations used by the lookup
  (exact → alias → singular fallback).

## Adding a term

```
python3 bin/add_glossarium_term.py path/to/term.md [--slug <code>]
make glossarium-index
```

The importer reads the name from the first `# ` heading, optional
`aliases: [...]` front matter, and stores the rest as the body.

## Select-a-word lookup

`app/js/glossarium-lookup.js` is included by the glossarium page, the note
catalog and viewer, and the live notes. On the first text selection it
lazy-loads `data/index.json`, matches the selection against names and aliases,
and shows a floating definition card near the selection with a link to the
full term. Every page injects its index path through the script's
`data-glossarium` attribute — always relative to that page, so prefix mounting
keeps working.
