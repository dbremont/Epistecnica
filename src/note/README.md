# Notes

> The written corpus behind Epistecnica's ontologies — technical objects,
> external systems, libraries, operations — indexed and served at `/note/`.

## Layout

```
src/note/
├── README.md        # this document
└── app/             # served statically at /note/
    ├── index.html   # catalog: dir browse/files + @tag search (+ pins)
    ├── note.html    # single-note viewer (?n=<path>)
    ├── notes.css    # markdown typography (shared design tokens)
    ├── vendor/      # vendored runtime deps (marked.min.js, alpine.min.js)
    ├── data/        # the corpus (never machine-edited) + generated index.json (do not edit)
    │   ├── index.json   # generated search index
    │   ├── changelog.json        # per-note edit history (hand-edited)
    │   ├── changelog.schema.json # schema for changelog.json
    │   ├── epistemica/  # epistemical notes (Modelling domains + elements; theory/ scope)
    │   ├── nature/      # natural notes (natural elements)
    │   └── technica/    # technical notes (cto/, pto/, op/, computation/)
```

- Regenerate the search index after any corpus change: `make notes-index`.
- Notes are plain markdown with zero required metadata: title comes from the
  first `# ` heading (else the filename); the top-level directory is the
  section (`epistemica`, `nature`, `technica`).

## Epistemica corpus

`data/epistemica/` holds the epistemical notes — the *Modelling* (Modelado)
domains (`causality.md`, `mathematical.md`, `observational.md`, …) and their
element notes, one directory per domain (`epistemica/mathematical/group.md`).
They document epistemic elements and must follow the epistemical schema (title,
intro quote, `## Formulation` with the three questions including the recursive
instance decomposition, `## References`) owned by the canonical philosophia
guide at
`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`;
the guide's Arithmetic case study is the worked exemplar, and the local
companion is `data/epistemica/ees.md`.

- The corpus was seeded from the Naturgnosis Notion *Modelado* export
  (one-off migration; the importer was removed after use — names
  normalized, CSV tags as front matter, Notion noise stripped; content
  preserved). The corpus is now the source of truth.
- The dynamical-systems notes live in the `epistemica/mathematical/ds/`
  scope (the *ds* sub-scope of the Mathematical domain); elements best kept
  separate (differential/difference equations, operators, SDE, phase/state
  space) are reached through `links.json` rather than moved into it.
- The mathematical spaces live in the `epistemica/mathematical/space/`
  scope, with `space/space.md` as the master note. Related foundational
  notes (structure, geometry, topology, order, measure, algebra, coordinate
  systems) stay in `mathematical/` and are reached through `links.json`.
- The validation scope lives in `epistemica/validation/`: `validation.md`
  (master), `probability-model-validation.md`, `calibration.md`,
  `statistical-hypothesis-testing.md`, `p-value.md`, `e-value.md`,
  `goodness-of-fit.md`, and `confidence-interval.md` (the procedure-coverage
  reporting member, moved out of the observational domain).
- The p-value atlas lives in `epistemica/validation/atlas/`:
  `pvalue.json` (the null-distribution store) and `pvalue.html` (the
  playground: pick a law, move its parameters and `t_obs`, read the live
  density/CDF tails, readouts and Monte Carlo calibration strip);
  `make pvalue-check` validates the store. Linked from `p-value.md`.
- The goodness-of-fit atlas lives beside it: `gof.json` (the law and
  discrepancy-measure store) and `gof.html` (the playground: pick a law and a
  measure, set `n` and the contamination `δ`, and read the empirical fit, the
  null cloud, the power curve and the p-value calibration); `make gof-check`
  validates the store. Linked from `goodness-of-fit.md`.
- The terminology-crimes atlas lives in `epistemica/crimes/`:
  `terminology.json` (the store) and `terminology.html` (searchable cards and
  table over misnomers, legacy names and false friends in statistics,
  probability and measurement); `make terminology-check` validates the store.
- Run `make notes-index` afterwards, as for any corpus edit.

## Computation corpus

`data/technica/computation/` holds the computation notes — the domain notes
(`algorithm.md`, `language-system.md`, `system.md`, …) and their element
notes, preserving the export's subcollection tree
(`computation/language-system/conceptual-model-language-system/python.md`).

- Imported mechanically from the Notion *Computacion* export (a one-off
  migration; the importer was not kept): names normalized, CSV tags as front
  matter, relation properties and note links rewritten for the viewer, images
  copied beside their note, Notion noise stripped; content preserved. The
  corpus is now the source of truth.
- The import is mechanical: the notes have not yet been converted to the
  technical schema owned by the canonical philosophia guide.
- Run `make notes-index` afterwards, as for any corpus edit.

## Theory corpus

`data/epistemica/theory/` holds the cross-domain theory notes: the
*Philosophia Naturalis* conceptual model imported from its Notion export —
the root guide (`theory/philosophia-naturalis.md`), `theory/philosophy.md`,
and its concept notes — together with the identifiability note
`theory/practice/modelling.md`.

- The imported notes keep the source's own template
  (Meta/Evaluation/Signature/QA) and have not been converted to the
  epistemical schema; `theory/practice/modelling.md` is authored in the
  epistemic-element schema.
- The imported conceptual model was migrated mechanically (a one-off
  migration; the importer was not kept): names normalized, CSV tags as front
  matter, relation properties rewritten as a `Related:` line, Notion noise
  stripped, images moved to the shared `/assets/` store; content preserved.
- `theory/practice/modelling.md` frames modelling as an identification
  diagram — map, connectors, observational equivalence, identifiability.
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
- **Toggles**: ★ pinned (browser-local pins, `localStorage`), live
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
  marked with a `live` chip. Examples: `technica/general/cto/lib/concurrent-map.html`
  ("Concurrent Map"),
  `epistemica/observational/distribution/atlas/poisson-distribution.html` ("Poisson Distribution"),
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
- Only content changes are logged. A metadata-only edit of the front matter
  (`tags:`, `qa:`) is not content, so it appends **no** log — the changelog
  records what the document says, not how its metadata is indexed.
- `bin/link_changelog_commits.py` (or `make changelog-link`) fills the
  optional `commit`/`before` shas **after** the change-set commit — the
  introducing sha is unknowable when the log is authored. Commit the
  json-only annotation separately. Going forward only.
- The documents and courses corpora keep the same changelog shape
  (`src/document/app/data/changelog.json`,
  `src/course/app/data/changelog.json`, schema beside each). Their history
  was backfilled from git by `bin/backfill_changelog.py`; change sets
  touching those corpora append logs the same way, and the same linker
  stamps them (`--corpus` selects one).
- The viewer shows a `history` chip when logs exist, opening a modal that
  lists them newest-first, each with `commit` / `before` / `after` links to
  `github.com/dbremont/Epistecnica`.
- The index builder ignores `*.json`, so changelog edits need no index
  rebuild. Git log remains the source of truth.

## Pins

The catalog lets you pin notes (star button per row, `pinned` facet chip).
Pins are browser-local: the catalog keeps them in `localStorage`
(`epistecnica.note-pins`), with no server call and no database. They are not shared
across browsers or devices, and the catalog filters out pins whose notes no
longer exist (the pin UI hides when `localStorage` is unavailable).

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

## QA questions

Front matter may also carry `qa:` — a block list of open reflection
questions, one per `- ` line (no inline form, so commas and colons inside a
question are safe):

```markdown
---
tags: [ai]
qa:
  - What technical element type does this instance belong to?
  - How does the scaling law justify the parameter count?
---

# Title
```

- The indexer copies a non-empty `qa` list into `data/index.json`; entries
  without questions omit the key.
- The viewer shows a `QA · N` chip in the metadata bar when the list is
  present; clicking it opens a modal listing the questions (no navigation).
  Questions may carry `$…$` TeX math; the notes viewer typesets them in the
  modal (MathJax ships with the note viewer only — other shells show the
  literal source).
- Nothing is inferred from the body: a `## QA` section is ordinary rendered
  content. Front matter is the metadata source, so questions are authored
  once, deliberately.
- The same convention applies to the courses and documents corpora.

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

`bin/notes_index.py` validates every note path and prints warnings for violations;
warnings never fail the build. Keep the output warning-free.
