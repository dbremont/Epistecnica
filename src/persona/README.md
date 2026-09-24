# Personas

> A new type of note — each persona entry carries a `type:` field
> (architecture, paper, and whatever the corpus grows next), plus tags —
> indexed and served at `/persona/`.

## Layout

```
src/persona/
├── README.md        # this document
├── bin/index.py     # search-index builder (stdlib only)
└── app/             # served statically at /persona/
    ├── index.html   # catalog: search + type + tag facets
    ├── persona.html # single-entry viewer (?p=<path>)
    ├── personas.css # markdown typography (shared design tokens)
    ├── data/        # generated (index.json — do not edit)
    └── personas/    # the corpus (never machine-edited)
```

- Regenerate the search index after any corpus change: `make persona-index`.
- Entries are plain markdown with one required metadata field: `type:`
  front matter (`---`-fenced, same style as the glossarium aliases),
  e.g. `type: architecture` or `type: paper`. The title comes from the
  first `# ` heading (else the filename). Missing or invalid types warn
  and fall back to `untyped`; the type vocabulary grows without code
  changes — catalog facets derive from the data.
- Optional `tags: [...]` front matter types each entry further; tags
  surface as catalog facets and viewer chips, and rank between
  headings and body text in search. See `src/note/README.md` for the
  shared tag convention.
- The viewer renders a type chip linking back to the type-filtered
  catalog (`index.html?type=<type>`); the catalog also accepts
  `?tag=` deep links.
- Markdown rendering uses the notes vendor bundle relatively
  (`../note/vendor/marked.min.js`) — no duplicated runtime deps.

## Naming convention

Same rules as the notes corpus (see `src/note/README.md`): ASCII only,
lowercase, kebab-case — for `.md` filenames, types, and tags.

`bin/index.py` validates every entry path, type, and tag and prints
warnings for violations; warnings never fail the build. Keep the output
warning-free.

## Import

One-off migration from the Notion "Catálogo de Personas" export:

```
python3 src/persona/bin/import.py <notion-export-dir>
python3 src/persona/bin/index.py
```

The importer strips Notion uuid suffixes and writes one `type: person`
entry per file (the export CSVs duplicate the md `tags:` lines and
carry only ordering noise, so they are deliberately not read). Bare
`: <number>` property lines, ellipsis-only (`> …`) placeholders, and
empty `## Index` headings are dropped; referenced images are copied
beside their entry with rewritten qualified links; colliding slugs get
a numeric suffix and existing files are never overwritten. Afterwards
the corpus under `app/personas/` is the source of truth — edit entries
by hand and rerun `make persona-index`.
