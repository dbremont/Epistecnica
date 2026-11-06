# Glossarium

> The lexical corpus behind Epistecnica — terms and definitions, one markdown
> file per term, indexed and served at `/glossarium/`, with select-a-word
> lookup on the note pages.

## Layout

```
src/glossarium/
├── README.md        # this document
└── app/             # served statically at /glossarium/
    ├── index.html       # catalog (search, letter facets) + term view (?t=<slug>)
    ├── glossarium.css   # markdown typography (shared design tokens)
    ├── js/              # select-a-word popup (also wired into the notes pages)
    ├── vendor/          # vendored runtime deps (marked.min.js)
    ├── terms/           # the corpus: one <slug>.md per term (source of truth)
    └── data/
        └── index.json   # generated lookup/search index (do not edit)
```

- The corpus is `app/terms/<slug>.md` — one readable markdown file per term,
  served as-is at `/glossarium/terms/<slug>.md` (the term view links it as
  `view raw`).
- Regenerate the derived index after any corpus change: `make glossarium-index`
  (`bin/build_glossarium_index.py`, chunked and progress-aware — the server can
  also rebuild it through `POST /api/index/build`).
- `data/index.json` is generated and gitignored; the Dockerfile rebuilds it.

## Term shape

```markdown
---
aliases: [tecnicidad]
---

# Technique

…the definition, in markdown…
```

- The filename stem is the `slug` (the term code): kebab-case ASCII, lowercase,
  runs of non-alphanumerics folded to `-` (the same rule as note filenames).
- The first `# ` heading is the `name` as displayed and indexed (fallback: the
  slug with dashes as spaces).
- Optional `aliases: [...]` front matter lists alternative spellings and
  translations used by the lookup (exact → alias → singular fallback). Front
  matter is emitted only when a term has aliases.
- Everything after the front matter is the body, rendered by the term view and
  indexed for search.

## Adding a term

```
python3 bin/add_glossarium_term.py path/to/term.md [--slug <code>]
make glossarium-index
```

The helper copies the file into `app/terms/<slug>.md` (slug from the filename
stem unless `--slug` is given), validating the kebab-case slug and the `# `
heading first. Writing the file into `app/terms/` by hand is equivalent — the
file *is* the term.

## Select-a-word lookup

`app/js/glossarium-lookup.js` is included by the glossarium page, the note
catalog and viewer, and the live notes. On the first text selection it
lazy-loads `data/index.json`, matches the selection against names and aliases,
and shows a floating definition card near the selection with a link to the
full term. Every page injects its index path through the script's
`data-glossarium` attribute — always relative to that page, so prefix mounting
keeps working.
