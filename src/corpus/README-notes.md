# Notes

> The written corpus behind Epistecnica's ontologies — technical objects,
> external systems, libraries, operations — indexed and served at `/corpus/notes`.

## Layout

```
src/corpus/
├── README-notes.md      # this document
├── app/                 # shared catalog + global viewer + generated data
│   ├── /explorer.html       # directory browser + section tree
│   ├── view.html        # global markdown viewer (?p=notes|documents|courses/…)
│   ├── corpus.css
│   ├── vendor/
│   └── data/            # generated indexes, changelogs, links.json
└── notes/               # the notes corpus (served at /corpus/notes)
    ├── epistemica/      # epistemic notes (Modelling domains + elements; theory/)
    ├── nature/          # natural notes (natural elements; theory/; human/)
    ├── technica/        # technical notes (cto/, pto/, op/, computation/, industry/, formation/)
    ├── social/          # social-reality notes
    ├── unclassified/    # essays and not-yet-filed material
    └── meta/            # schemas, guides, atlases
```

- Regenerate the search index after any corpus change: `make notes-index`.
- Notes are plain markdown with zero required metadata: title comes from the
  first `# ` heading (else the filename); the top-level directory is the
  section (`epistemica`, `nature`, `technica`, `social`, `unclassified`,
  `meta`). The former `human/` section is now `nature/human/`, the former
  `history/` section is now `social/history/`, and the former `essays/`
  section is now `unclassified/`.

## Merged Naturgnosis corpus

The Naturgnosis note space was merged into this corpus (2026-11-02). The
filing rules that shaped it:

- `nature/` and `epistemica/` merge in place; `social/` (including
  `social/history/`), `unclassified/` and `meta/` are their own sections. The
  former `human/` section was later folded into `nature/human/` (2026-11-06).
- `technique/` became `technica/`: industrial, material, energy and
  production notes live under `technica/general/cto/industry/`, technical
  domain sets under `technica/general/cto/es/multinode/`, and formation
  institutions (schools, universities) under
  `technica/general/op/formation/`.
- `general/` and `miscellanea/` became `unclassified/` (initially `essays/`).
- `data-collection/` moved under `epistemica/data/`.
- On collisions the Epistecnica note was kept and the incoming file skipped
  (same destination path, or same section + title). Links were rewritten
  through the resulting path map, so no note carries a stale Naturgnosis
  path; corpus images moved to the shared asset store as usual.
- The import appended no changelog logs: it is provenance, not an edit, so
  migrated notes have no history entries of their own until their next change.
- `meta/` mirrors the canonical philosophia guides locally; the raw
  Naturgnosis URLs stay the canonical citations in prose.

## Epistemica corpus

`/corpus/notes/epistemica/` holds the epistemical notes — the *Modelling* (Modelado)
domains (`causality.md`, `mathematical.md`, `observational.md`, …) and their
element notes, one directory per domain (`epistemica/mathematical/group.md`).
They document epistemic elements and must follow the epistemical schema (title,
intro quote, `## Formulation` with the three questions including the recursive
instance decomposition, `## References`) owned by the canonical philosophia
guide at
`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`;
the guide's Arithmetic case study is the worked exemplar, and the local
companion is `/corpus/notes/epistemica/ees.md`.

- The corpus was seeded from the Naturgnosis Notion *Modelado* export
  (one-off migration; the importer was removed after use — names
  normalized, CSV tags as front matter, Notion noise stripped; content
  preserved). The corpus is now the source of truth.
- The mathematical domain is filed by branch under
  `epistemica/mathematical/`: `structure/` (the algebraic and linear frame:
  `algebra/` for structures, `linear/` for vector spaces, matrices and operator
  maps, `category.md` for the language of structures, `duality.md`), `tensor/`
  (the tensor and the tensor fields built on it: metric, Riemann, Ricci,
  Einstein, Weyl, stress-energy, electromagnetic, stress, inertia),
  `number/` (numeral systems and the
  arithmetic transformation rules), `classical/` (the classical
  Greco-Roman tradition and its elementary toolkit: Euclidean geometry,
  classical algebra, equation solving, arithmetic computation), `discrete/` (combinatorics and discrete
  structures), `topology/`, `complex/` (the numeral system ℂ and the functions
  defined over it), `mapping/` (the kinds of map — `map.md` — and the
  functions they define: special functions and transforms), `equation/`,
  `change/` (dynamical representational
  systems), `space/`, `geometry/`, `construction/` (stated results), `method/`
  (routines, filed by what they do to the problem: `proof/`, `reduction/`,
  `approximation/`, `transform/`, `certify/`), and `transformation.md` at the
  root — the catalogue of the
  rewrite licences the representational systems carry. Notes that cut across
  branches (`set`, `relation`, `order`, `operator`, `decomposition`, `scale`)
  stay at the domain root.
- The change notes live in the
  `epistemica/mathematical/change/` scope (the dynamical-systems
  sub-scope of the Mathematical domain): the dynamical representational
  systems (differential, difference and recurrence equations, the
  differentiation operators, stochastic differential equations) beside the
  attractors, maps, and flows. Phase space (`science/phase-space.md`) and
  state-space models (`construction/state-space-model.md`) stay in their own
  scopes and are reached through note links — the scope no longer carries a
  `links.json` group.
- The mathematical spaces live in the `epistemica/mathematical/space/`
  scope, with `space/space.md` as the master note. Related foundational
  notes (structure, geometry, topology, order, measure, algebra, coordinate
  systems) stay in `mathematical/` and are reached through `links.json`.
- The singular scope lives in `epistemica/singular/`: the former `science/`
  scope (renamed from `computational-science/`) — the physical theories and
  frameworks (quantum field theory, statistical mechanics, gauge theory, the
  classical field theories, the mechanical formulations), the domain's
  spaces, systems, and elements, and the numerical and simulation methods used
  on them — together with the notes that bind one particular epistemic-element
  instance (`firm-clustering`, `firm-profiling`, `industry-analysis`,
  `swe-productivity`, `problematization`, …). The root keeps the domain
  catalogues, the master `ees.md`, and the general forms such as
  `production-function`.
- The construction scope lives in `epistemica/construction/`: the named
  constructions — the theories, laws, and models stated about particular
  systems (Navier–Stokes, Fick's laws, Lotka–Volterra, general equilibrium,
  DFT, molecular-orbital theory, the Mori–Zwanzig formalism, …) — split out of
  the science scope.
- The validation scope lives in `epistemica/validation/`: `validation.md`
  (master), `probability-model-validation.md`, `calibration.md`,
  `statistical-hypothesis-testing.md`, `p-value.md`, `e-value.md`,
  `goodness-of-fit.md`, and `confidence-interval.md` (the procedure-coverage
  reporting member, moved out of the observational domain).
- The quantification scope lives in `epistemica/quantification/` (the former
  `epistemica/measurement/`, renamed when the quantification note joined it):
  `quantification.md` (the representational scheme that binds a magnitude to a
  number -- a scale, a unit, a numeral; the scope master, moved in from
  `epistemica/mathematical/number/`), `measurement-theory.md` (measurement as a
  structure-preserving assignment of numbers to attributes; the representation
  and procedure problems), `system.md` (the constellation of units, standards
  and rules a body of work measures with), and `isu.md` (the International
  System of Units). Measurement theory moved out of the science scope with the
  first note of the scope; the technica performance `measure.md` points here.
  Quantization -- the discretization that replaces a continuum value by one of
  finitely many levels -- is the scheme's downstream neighbour and stays in
  `epistemica/mathematical/quantization.md`; the two are distinguished in both
  notes' tables. `epistemica/mathematical/number/quantification.md` is a
  symlink kept at the note's former address -- the indexer skips symlinks, so
  it never becomes a second corpus entry.
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
- The terminology atlas lives in `epistemica/horror/`:
  `terminology.json` (the store) and `terminology.html` (searchable cards and
  table over misnomers, legacy names and false friends in statistics,
  probability and measurement); `make terminology-check` validates the store.
- Cross-cutting method families are carried as tags, not scopes. The former
  `natural-computing/` scope was dissolved into the scope that owns each note's
  operation — the evolutionary and swarm optimizers into `optimization/`,
  cellular automata into `mathematical/change/`, swarm intelligence and
  self-organized criticality into `complexity/`, flux balance analysis into
  `construction/` — and its members carry `tags: [natural-computing]`. A
  metaphor for the method's inspiration is an attribute, not a target: give it
  a tag instead of a directory.
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

## Human corpus

`data/nature/human/human/` holds the human cognition and behaviour notes migrated
from the Notion *Human* space. They live under `nature/` because their object
is the human natural system; the subsection keeps the source's collection tree
(`nature/human/cognitive/conceptual-model-cognition/...`).

- The section masters (`human`, `cognitive`, `behavioral`) and the element
  notes whose natural counterpart already existed (`attention`, `emotion`,
  `language`, `learning`, `linguistics`, `motor-control`, `perception`,
  `reference`, `social-cognition`, `connectome`) were merged into the
  `nature/` notes of the same name (2026-11-06). The merged notes keep the
  naturalis schema shell — title, intro quote, `## Formulation` with the three
  questions, `## References` — with the imported sections following
  `Formulation` and the human definition replacing the "not yet worked"
  placeholder.
- The rest of the subtree was moved verbatim and its links re-pointed from
  `human/…` to `nature/human/…`; every moved note carries a `refactor`
  changelog log for the move.
- Run `make notes-index` afterwards, as for any corpus edit.

## Theory corpus

`/corpus/notes/epistemica/epistemic/theory/` is the flattened epistemic-theory scope:
`theory/philosophy.md`, the identifiability note `theory/modelling.md`,
and the former `theory/practice/` notes.

`/corpus/notes/epistemica/epistemic/guidance/` holds what grounds and guides inquiry:
the ontic condition notes at its root (`equilibrium`, `stable`, …),
`guidance/principle/` for rules of proceeding (`occam-razor`,
`minimum-description-length-mdl`, …), and `guidance/method/` for the
philosophical-method notes.

`/corpus/notes/epistemica/epistemic/discipline/` holds the discipline catalogues
(mathematics, statistics, computer science, …).

`data/nature/theory/` holds the natural-ontology theory scope: the ontic
element notes (event, causality, system, segment, reality, …), the local
*Philosophia Naturalis* guide (`theory/philosophia-naturalis.md`), and the
Change note.

- The imported notes keep the source's own template
  (Meta/Evaluation/Signature/QA) and have not been converted to the
  epistemical schema; `theory/modelling.md` is authored in the
  epistemic-element schema.
- The imported conceptual model was migrated mechanically (a one-off
  migration; the importer was not kept): names normalized, CSV tags as front
  matter, relation properties rewritten as a `Related:` line, Notion noise
  stripped, images moved to the shared `/assets/` store; content preserved.
- `theory/modelling.md` frames modelling as an identification
  diagram — map, connectors, observational equivalence, identifiability.
- Run `make notes-index` afterwards, as for any corpus edit.

## Catalog

`/explorer.html` follows the Naturgnosis catalog model (the same engine is
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
  `/view.html?p=notes/<path>`. The bulk of the corpus.
- A **live note** is a self-contained, hand-authored HTML page (`*.html`),
  co-located with its companion markdown note — bespoke interactivity, its
  own scripts. Served as-is; never rendered through the viewer. Every live
  note uses the same frame as the viewer (`view.html`: ambient constellation
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
  `epistemica/observational/process/hawkes-process.html` ("Hawkes Process"),
  `epistemica/observational/process/fokker-planck-equation.html`
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
  (`src/corpus/app/data/changelog.notes.json`,
  `src/corpus/app/data/changelog.notes.json`, schema beside each). Their history
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

Every note carries `note` as its **first** tag, so the top-level corpus is
visible in search and in the viewer. Additional tags follow it:

```markdown
---
tags: [note, java, debugging, osgi]
---

# Title
```

- Tags follow the same naming rules as paths: ASCII, lowercase,
  kebab-case. The indexer warns on violations and drops the bad tag.
- Tags are indexed into `src/corpus/app/data/notes-index.json`, surface as `@tag` search tokens
  and as viewer chips (`?q=@<tag>` deep links), and rank between headings
  and body text in search.
- The same convention applies to the courses corpus
  (`src/corpus/README-courses.md`) and the documents corpus
  (`src/corpus/README-documents.md`).

## Order

Front matter may carry `order:` — a **natural number** (0, 1, 2, …) that sets
the note's render position among the files of its directory:

```markdown
---
order: 0
---

# Title
```

- Lower numbers render first. Notes without `order:` come after every
  ordered note and keep the index (path) order; folders always render before
  files, and folders themselves are never ordered.
- The indexer copies a valid value into `src/corpus/app/data/notes-index.json` as `order`;
  anything that is not a natural number warns and is dropped.
- Search orders by relevance first; `order` (then title) breaks ties.
- Notes corpus only for now — the documents, courses, and personas catalogs
  do not read the field.

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

- The indexer copies a non-empty `qa` list into `src/corpus/app/data/notes-index.json`; entries
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
overlay. The registry is tracked (unlike the generated indexes): edit it,
then rebuild the index.

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
