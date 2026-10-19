# Notes

> The written corpus behind Epistecnica's ontologies — technical objects,
> external systems, libraries, operations — indexed and served at `/note/`.

## Layout

```
src/note/
├── README.md        # this document
├── bin/index.py     # search-index builder (stdlib only)
└── app/             # served statically at /note/
    ├── index.html   # catalog: dir browse/files + @tag search (+ pins)
    ├── note.html    # single-note viewer (?n=<path>)
    ├── notes.css    # markdown typography (shared design tokens)
    ├── vendor/      # vendored runtime deps (marked.min.js, alpine.min.js)
    ├── data/        # the corpus (never machine-edited) + generated index.json (do not edit)
    │   ├── index.json   # generated search index
    │   ├── changelog.json        # per-note edit history (hand-edited)
    │   ├── changelog.schema.json # schema for changelog.json
    │   ├── general/     # shared notes (philosophiae, companions)
    │   ├── epistemica/  # epistemical notes (Modelling domains + elements)
    │   └── technica/    # technical notes (cto/, pto/, op/)
```

- Regenerate the search index after any corpus change: `make notes-index`.
- Notes are plain markdown with zero required metadata: title comes from the
  first `# ` heading (else the filename); the top-level directory is the
  section (`general`, `technica`, …).

## Epistemica corpus

`data/epistemica/` holds the epistemical notes — the *Modelling* (Modelado)
domains (`causality.md`, `mathematical.md`, `observational.md`, …) and their
element notes, one directory per domain (`epistemica/mathematical/group.md`).
They document epistemic elements and must follow the epistemical schema (title,
intro quote, `## Formulation` with the three questions including the recursive
instance decomposition, `## References`) owned by the canonical philosophia
guide at
`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`;
the worked exemplar is `data/general/financial-sector.md`.

- The corpus was seeded from the Naturgnosis Notion *Modelado* export with
  `bin/import_epistemica.py <export-root>` (names normalized, CSV tags as
  front matter, Notion noise stripped; content preserved). Re-running skips
  existing notes.
- The dynamical-systems notes live in the `epistemica/mathematical/ds/`
  scope (the *ds* sub-scope of the Mathematical domain); elements best kept
  separate (differential/difference equations, operators, SDE, phase/state
  space) are reached through `links.json` rather than moved into it.
- Run `make notes-index` afterwards, as for any corpus edit.

## Catalog

`index.html` follows the Naturgnosis catalog model (the same engine is
mirrored in the courses and documents catalogs). There are no section/tag
facet bars: sections are reached as folders and tags through the search box.

- **Search** (`?q=` deep link, prefilled): free text ranked title > headings
  > tags > body, plus `@tag` tokens — each an exact, case-insensitive tag
  filter (AND). Typing `@` opens an autocomplete menu of corpus tags.
  `ctrl + /` focuses the box (`/` focuses the hub's universal search).
- **Views** (`?view=browse|files`, default `browse`): browse mixes folder
  cards (a subdirectory, with a count) with the files directly inside the
  current directory; files flattens the whole corpus (or the `?dir=` scope).
- **Directory** (`?dir=<scope>`): entering a folder card, or an ancestor
  breadcrumb, changes the listing in place via `pushState` — no reload.
- **Toggles**: ★ pinned (server pins, `GET/POST /note/api/pins`), live
  (`?live=1`), unfinished (`?unfinished=1`, notes tagged `unfinished`).

## Notes vs live notes

- A **note** is a markdown file (`*.md`): rendered on the fly by
  `note.html?n=<path>`. The bulk of the corpus.
- A **live note** is a self-contained, hand-authored HTML page (`*.html`),
  co-located with its companion markdown note — bespoke interactivity, its
  own scripts. Served as-is; never rendered through the viewer. Every live
  note uses the same frame as the viewer (`note.html`: ambient constellation
  background, 1280px layout, crumbs + title + meta chips, card, sticky
  `Contents` sidebar) and the philosophia shell order (intro quote,
  Index, Formulation, decomposition, lab, Diagnostic questions,
  References) with `.markdown-body` typography — so live notes read as
  part of the site, not as foreign pages. The canonical copy-paste
  chrome blocks plus the container spec and conversion record live in
  `docs/live-note-chrome.md`; no CDN libraries are allowed. The catalog
  still indexes it (title, headings, text) and links directly to the page,
  marked with a `live` chip. Examples: `technica/cto/lib/concurrent-map.html`
  ("Concurrent Map"),
  `epistemica/observational/poisson-distribution.html` ("Poisson Distribution"),
  `epistemica/observational/hawkes-process.html` ("Hawkes Process"),
  `epistemica/observational/fokker-planck-equation.html`
  ("Fokker-Planck Equation").

## Changelog / history

Every markdown note carries a per-file edit history in
`app/data/changelog.json` (with `changelog.schema.json`): an array of
`{file_path, logs[]}` objects, `file_path` a corpus-relative `.md` path
(live HTML and other assets are out of scope). Each log is
`{date: YYYY-MM-DD, summary; optional kind}` — commit-type words like
`feat`/`fix`/`docs` suggested. Object key order follows the schema's
`properties` order.

- Every change set touching `app/data/**/*.md` appends one log per touched
  note, **in the same commit**; validate with
  `python3 -m json.tool app/data/changelog.json`.
- `bin/link_changelog_commits.py` (or `make changelog-link`) fills the
  optional `commit`/`before` shas **after** the change-set commit — the
  introducing sha is unknowable when the log is authored. Commit the
  json-only annotation separately. Going forward only.
- The viewer shows a `history` chip when logs exist, opening a modal that
  lists them newest-first, each with `commit` / `before` / `after` links to
  `github.com/dbremont/Epistecnica`.
- The index builder ignores `*.json`, so changelog edits need no index
  rebuild. Git log remains the source of truth.

## Pins

The catalog lets you pin notes (star button per row, `pinned` facet chip).
Pins are server-side, not per-browser: `GET/POST /note/api/pins` (served by
`bin/serve.py`) reads and upserts a single `pins` doc in the CouchDB
database named by `NOTES_DB` (default `notes`; created by `make bootstrap`).
The server validates paths against the corpus naming rules; the catalog
hides the pin UI when the API is unreachable and filters out pins whose
notes no longer exist.

## Tags

Notes accept optional `tags: [...]` front matter, `---`-fenced at the top
of the file (the same `---` front-matter style used across the corpora):

```markdown
---
tags: [java, debugging, osgi]
---

# Title
```

- Tags follow the same naming rules as paths: ASCII, lowercase,
  kebab-case. The indexer warns on violations and drops the bad tag.
- Tags are indexed into `data/index.json`, surface as `@tag` search tokens
  and as viewer chips (`?q=@<tag>` deep links), and rank between headings
  and body text in search.
- The same convention applies to the courses corpus
  (`src/course/README.md`) and the documents corpus
  (`src/document/README.md`).

## Support links

`app/data/links.json` is the single hand-maintained registry of directed
navigation links — `{"links": [{"from", "to", "label", "kind"}]}`; endpoints
are note paths or `dir/` scopes (`from` a directory node, `to` a directory or
a note). The builder validates every endpoint against the corpus (warn and
drop dangling, never fail) and embeds the pairs as `index.json:links`; the
catalog's browse view renders them as a linked group of cards with a link-mark
overlay. Edit the registry, then rebuild and commit the index.

- The registry is a special file: never a note, never naming-validated.
- `kind` is a free-form tag (`hierarchy`, `related`, …); `label` names the
  target and is shown as a card badge.

## Naming convention

Note paths (directories and `.md`/`.html` filenames) must be:

- **ASCII** only — `a-z`, `0-9`, `-` (no accents, spaces, underscores, dots
  beyond the `.md`/`.html` extension)
- **lowercase** — never capitals
- **kebab-case** — words separated by `-`

Examples: `vlc-media-player.md`, `ssh-config.md`, `apache-kafka.md`,
`berkeley-packet-filter-bpf.md`. Non-markdown assets (images, code samples)
may live beside notes and are exempt from the filename rule, but directories
always follow it.

`bin/index.py` validates every note path and prints warnings for violations;
warnings never fail the build. Keep the output warning-free.
