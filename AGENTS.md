# AGENTS.md — notes for coding agents working in this repo

Epistecnica is a hub for the project's corpora — notes, courses, documents —
served by one combined server from one deployment, under one guide-first entry
page. The ontology graphs (epistemica, tecnica) no longer live here: they moved
to the external **Autoregia Personal Knowledge System** (`http://localhost:8088/pks/`),
and the hub points at it.

## What this is

- **The guide** — the project's philosophia guides (epistemicarum +
  technicarum) are the canonical schema owners; the hub foregrounds them and
  the local EES atlas (`src/corpus/notes/epistemica/ees.html`) is their
  local companion.
- **Index** — **Autoregia**, the Personal Knowledge System
  (`http://localhost:8088/pks/`) owns the master index and the ontology
  graphs; the hub links to it from its entry index, and the old local graph
  apps were retired (their URLs 302). The lexical corpus (glossarium) and the
  Q/A log are served locally next to the note corpus (`/glossarium/`, `/qa/`),
  which now also carries the natural material (including the human corpus —
  body, physiology, mind, cognition and behaviour — under `nature/human/`),
  social, historical and essay
  material migrated from the Naturgnosis note space.
- **Corpora** — `src/corpus/notes`, `src/corpus/courses`, `src/corpus/documents`: catalogs + viewers
  over a local markdown corpus, with generated JSON indexes.
- No Node build step, no test suite; Python-stdlib servers in `bin/`, vanilla
  JS. Do not introduce package managers, frameworks, or build steps.

## Repo map

```
index.html              hub (served at /)
bin/                    every repo script lives here (centralized — never under src/; see Tooling notes)
bin/serve.py            combined server — the only frontend-facing surface; owns all routes below
bin/envutil.py          .env loader
bin/indexlib.py         shared index-build plumbing (chunked progress, atomic writes, status file)
bin/index_jobs.py       index-build runner (dependency order, single-flight, background jobs)
bin/build_glossarium_index.py  glossarium lookup/search index (terms/*.md → index.json)
bin/add_glossarium_term.py     add/replace one glossarium term (copies into terms/)
bin/build_qa_index.py  Q/A log search index (qa.json → qa-index.json)
bin/notes_index.py | bin/course_index.py | bin/document_index.py   corpus indexers (make *-index)
bin/course_import.py | bin/document_import.py   bulk Notion-export importers
bin/rees_check.py | bin/atlas_check.py | bin/terminology_check.py | bin/symbols_check.py | bin/pvalue_check.py   atlas/store validators (make *-check)
bin/conform.py          technica table-grammar conformance; bin/build_technica_atlas.py atlas builder
src/app/                hub (index.html, /) + explorer.html (directory explorer) +
                            view.html (global viewer) + docs.html + corpus.css +
                            vendor/ + data/ (generated indexes, changelogs, links)
                            + shared/ (nav search + viewer script + index chip)
src/corpus/             content only: notes/ (sections + live notes), documents/
                            (papers, articles, books), courses/ (course dirs with
                            readme.md + lectures); the three READMEs sit here
src/glossarium/…        lexical corpus + catalog/term view + lookup popup — see src/glossarium/README.md
src/qa/…                Q/A log + catalog/entry viewer — see src/qa/README.md
spec/                   general spec + shared design system + epistemic-content extraction method
docs/                   documentation hub
Makefile, Dockerfile    project operations (make run/check/build/deploy-*/logs/stop) + combined image
.github/workflows/      one workflow building ghcr.io/dbremont/epistecnica
```

## Architecture contract (do not break)

**The browser only talks to `bin/serve.py`.** The combined server is the only
frontend-facing surface in the deployment; there is no database behind it
(the notes-catalog pins are browser-local).

- Routes served by `bin/serve.py`:
  - `/` → hub `src/app/index.html`
  - `/docs` (also `/docs/`, `/docs.html`) → site documentation `src/app/docs.html` — the single user-facing docs surface (theory + guide, live stats from the APIs); the old per-subproject docs pages were deleted
  - `/explorer.html` (also `/notes`) → the directory explorer `src/app/explorer.html` — browse/folders over notes + documents + courses, built from `src/app/data/library-index.json`, with search, pins and filters; `/corpus` and `/library` 302 here
  - `/shared/<path>` → static from `src/app/shared/<path>` (the universal nav search — `usearch.css` + `usearch.js` — included by every surface; plus the shared content-viewer script `viewer.js` behind the single corpus viewer)
  - `/assets/<path>` → static from `src/app/assets/<path>` (the shared corpus-image store: every image referenced by corpus markdown lives here — `note/…`, `course/…`, `document/…` subtrees mirroring the corpus paths, plus a few generic diagrams at the root — never beside the notes)
  - `/view.html` → the global markdown viewer `src/app/view.html` (`?p=notes|documents|courses/…`), replacing the old note/document/course/lecture shells; `/note.html` serves the same page as a legacy alias
  - `/corpus/notes/…`, `/corpus/documents/…`, `/corpus/courses/…` → the content trees under `src/corpus/<tree>/`, served as-is; the catalog app (`explorer.html`, `view.html`, `corpus.css`, `vendor/`, `data/`) lives in `src/app/`
  - `/epistemica/<path>` and `/tecnica/<path>` → **302** to
    `/corpus/notes/epistemica/ees.html` (the graphs moved to the Autoregia PKS)
  - `/corpus/notes/epistemica/rees.{html,json,md}` → **302** to the `ees.*`
    equivalents (legacy REES paths)
  - `/favicon.ico` → **302** to `/img/favicon.ico`. Only the hub and graph
    pages carry an explicit `<link rel="icon">`; every other surface relies on
    the browser's default host-root probe, which would otherwise 404. Route it
    to the real asset instead of touching ~34 HTML pages. The light-mode nav
    mark swap (`img/mark-gold-dark.png`) is CSS-only, in
    `src/app/shared/usearch.css`.
  - `/glossarium/<path>` → static from `src/glossarium/app/<path>` (the lexical
    corpus: catalog + term view at `?t=<slug>`, the generated lookup index and
    the select-a-word popup every note page loads relatively)
  - `/qa/<path>` → static from `src/qa/app/<path>` (the Q/A log: catalog +
    entry viewer at `?id=<qa-id>`)
  - `/api/health` → liveness probe for the service
  - `/api/index/status` → live index-build progress (`{busy, job, builders}`);
    served only when `EPISTECNICA_ALLOW_INDEX_API=1`
  - `/api/index/build` → `POST` queues a chunked background rebuild and returns
    `202` at once (`409` when one is already running); same opt-in gate
- **Index builds are asynchronous.** `bin/index_jobs.py` runs the builders in
  dependency order in one background thread, each one chunked and reporting
  `done/total/pct` into the gitignored `src/app/data/index-status.json`. No
  surface waits for a rebuild: pages keep serving the last index and the shared
  `src/app/shared/index-status.js` chip shows progress while a job runs. The
  route is opt-in (`EPISTECNICA_ALLOW_INDEX_API=1`, set by `make run`) so the
  public deployment cannot be pushed into CPU-heavy rebuilds; the image still
  ships prebuilt indexes (`Dockerfile` runs the runner).
- Frontend pages fetch **relatively** (`api/…`, `data/…`) — that is what makes
  prefix mounting work without touching the huge HTML files. Keep it that way:
  never introduce absolute `/api/...` or `/data/...` paths in page code.
- **Catalogs and viewers render data, never literals.** The notes, courses, and
  documents catalogs and the shared viewer are generic renderers over the
  corpus indexes (`data/index.json`, the search snapshot), the hand-maintained
  `data/links.json` registry, and the corpus files those name. Never hardcode
  a corpus entry, section
  name, directory, note title, or href to a corpus artifact in page code — no
  promoted cards, no `state.dir === '<name>'` special cases, no literal
  `data/<corpus>/…` links. To surface something, put it in the data (the
  indexer, `links.json`) or write it in the docs/hub surface; when a rendered
  card looks wrong, fix the data, not the viewer. `bin/check_catalog_literals.py`
  (part of `make check`) enforces this on the three catalog pages. Page chrome
  (nav labels, links to other app surfaces) and the hub's curated entry links
  are not corpus listings and stay allowed.
- Corpus **images** live in `src/app/assets/` (served at `/assets/…`), never
  beside the notes. Reference them page-root-relative as
  `../assets/<corpus>/<path>` — the global viewer sits at `/view.html`,
  so one `../assets/…` reaches the shared store from every corpus and still
  works under prefix mounting. The whole corpus was migrated there (notes
  `assets/…` dirs and the beside-the-note course/document images); do not add
  per-note `assets/` dirs back.
- `.env` carries repo-local configuration (the deploy port) and is gitignored;
  it must stay that way.

## On Notes In General

- Filenames stay ASCII lowercase kebab-case; titles come from the first `# `
  heading. Every markdown file in the three content corpora carries its
  top-level corpus tag as the **first** tag — `note` under `src/corpus/notes`,
  `document` under `src/corpus/documents`, `course` under `src/corpus/courses`;
  `bin/check_corpus_tags.py` (part of `make check`) enforces it. Per-corpus
  naming/tags rules live in their READMEs
  (`src/corpus/README-notes.md`, `src/corpus/README-courses.md`, `src/corpus/README-documents.md`,
  `src/glossarium/README.md`, `src/qa/README.md`).
- `data/epistemica/epistemic/theory/` is the flattened epistemic-theory scope:
  `theory/philosophy.md`, the identifiability note `theory/modelling.md`
  (epistemic-element schema), and the former `theory/practice/` notes.
- `data/epistemica/epistemic/guidance/` holds what grounds and guides inquiry:
  the ontic condition notes at its root (`equilibrium`, `stable`, …),
  `guidance/principle/` for rules of proceeding (`occam-razor`,
  `minimum-description-length-mdl`, `least-action-principle`, …), and
  `guidance/method/` for the philosophical-method notes.
- `data/epistemica/epistemic/discipline/` holds the discipline catalogues
  (mathematics, statistics, computer science, …).
- A directory under `data/epistemica/` is a **target/operation scope**, not a
  metaphor: a cross-cutting method family is a tag. The former
  `natural-computing/` scope was dissolved on 2026-10-31 into the scopes that
  own each note's operation (`optimization/` for the evolutionary and swarm
  optimizers, `complexity/` for swarm intelligence and self-organized
  criticality, `mathematical/change/` for cellular automata, `construction/` for
  flux balance analysis) and its members carry `tags: [natural-computing]`; do
  not reintroduce it.
- The mathematical domain is filed by branch: `structure/` (`algebra/`,
  `linear/`, `category.md`, `duality.md`), `tensor/` (tensor and tensor
  fields), `number/`, `classical/` (the classical Greco-Roman tradition and
  its elementary toolkit: Euclidean geometry, classical algebra, equation
  solving, arithmetic computation), `discrete/`, `topology/`, `complex/`, `mapping/`
  (functions and maps — the functional relations), `relation/` (relations that
  are not functional: `relation`, `order`, `equivalence-relation`, `lattice`,
  `ranking`, `inequality`),
  `equation/`, `change/`, `space/`, `metric/`, `measure/`, `norm/` (the norm
  family, with `norm.md` as its central note and `order: 0`),
  `geometry/`, `construction/`, `method/` (filed by what a routine does to the
  problem: `proof/`, `reduction/`, `approximation/`, `transform/`, `certify/`),
  with `transformation.md` at the domain root. A new mathematical note goes in
  the branch that owns the object it is about — a *rule* (multiplication,
  differentiation) is a `Transformation Rule` of a representational system,
  never an "operator" note and never an act; see `mathematical/transformation.md`.
- `data/nature/theory/` holds the natural-ontology theory scope moved out of
  `epistemica/theory/ontology/`: the ontic element notes (event, causality,
  system, segment, reality, …), the local *Philosophia Naturalis* import
  (`theory/philosophia-naturalis.md`), and the Change note. The imported
  notes keep the source template and have no philosophia schema conversion.
- Regenerate the corpus index after any edit: `make index` (all of them),
  or individually `make notes-index`,
  `make course-index`, `make document-index`, `make glossarium-index`,
  `make qa-index`
  (see verification list below).
- Every change set touching `src/corpus/notes/**/*.md` appends one log per
  file to `src/app/data/changelog.notes.json` (schema beside it) **in the same
  commit**; then stamp `commit`/`before` post-commit with
  `python3 bin/link_changelog_commits.py`, commit the json-only annotation.
  The documents and courses corpora keep the same shape
  (`src/app/data/changelog.json`,
  `src/app/data/changelog.json`, schema beside each); their history
  was backfilled from git by `bin/backfill_changelog.py`, new change sets
  append logs there the same way, and
  `bin/link_changelog_commits.py --corpus document|course` stamps them.
  Only content changes are logged: a metadata-only edit of the front matter
  (`tags:`, `qa:`) appends **no** changelog log. Every viewer (`note`,
  `course`, `lecture`, `document`) shows the `history` chip. See
  `src/corpus/README-notes.md` §Changelog / history.
- Front matter may carry `qa:` — a block list of open reflection questions,
  one per `- ` line. The indexers copy a non-empty list into the corpus
  index (`qa` key), and every viewer shows a `QA · N` chip in the metadata
  bar that opens the question list. A body `## QA` section is rendered
  content, never the metadata source. See `src/corpus/README-notes.md` §QA
  questions.
- Notes front matter may also carry `order:` — a natural number giving the
  note's render position among the files of its directory (lower first;
  un-ordered notes follow in path order; folders always render before files
  and are never ordered). The notes indexer copies it into the index
  (`order` key), the notes catalog lists by it, and search uses it as the
  relevance tie-break. Notes corpus only. See `src/corpus/README-notes.md` §Order.
- Live notes (`src/corpus/notes/**/*.html`, co-located with their companion
  note) share the `view.html` frame
  (ambient background, layout, crumbs/title/meta, card, `Contents` sidebar)
  and the philosophia shell order — recipe + conversion record in
  `docs/live-note-chrome.md` §7–§8. They also carry the shared nav search
  (`/shared/usearch.css|js`, with `data-root` set to the file's own prefix to
  the site root). Keep `<title>`/h1, copy, and JS ids stable; the catalog
  indexes them.
- Page shells follow the note viewer: `max-width: 1280px; margin: 0 auto;
  padding: 2.5rem 2rem 3.5rem` (`.layout`); the hub is the one wide-system
  exception at 1200px.
- Math is typeset with the vendored MathJax 3 (`src/app/vendor/mathjax/`,
  configured by `src/app/vendor/mathjax-setup.js`). Author page math as
  `data-tex` / `data-tex-display` attributes (not raw `$…$`) so `bin/notes_index.py`
  never indexes LaTeX; corpus `.md` keeps literal `$…$`. Call `renderTeX()`
  after dynamic DOM updates. Recipe in `docs/live-note-chrome.md` §Vendored
  runtime dependencies.
- Playground live notes (`…/rsp/<system>.html`) are lean: intro → the
  instance's rate law + description → lab; no Formulation/decomposition
  sections. The phase plane opens on the **initial state** (no trajectories)
  and reveals as the user plays/steps.

## On Technical Notes

- **Discipline notes** live in `technica/discipline/` — one note per technical
  practice or technique, each with the technica shell and its own
  decomposition table. The engineering family: `geotechnical-engineering.md`
  (the ground as support and container), `structural-mechanics.md` (the load
  path above the foundation), and the two techniques the latter carries —
  `stability-analysis.md` (`Constitutive Technique`: eigenvalue, limit
  equilibrium, energy) and `euler-bernoulli-beam-theory.md`
  (`Technical Principle`: `EI w⁗ = q`, its assumptions and bounds). The
  structure such a practice designs is read naturally as a `Natural Object` —
  `nature/physical-object/structure.md`, the discrete body whose parts are
  held by a load path — never as a second technica root.

Multinode notes (`src/corpus/notes/technica/general/cto/es/multinode/`, e.g. `openapi.md`,
`wildfly.md`, `jobrunr.md`) document one technical
instance with the shell from the canonical technica guide
(`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md`)
(`# …` / intro / three Formulation questions / References) plus a single
instance-decomposition table:

- Pre-read: before writing any technical-element note, read
  the canonical technica guide above
  first — it owns the shell below, the Tabular taxonomy, the Recursive-view
  grammar, the decomposition contract, and the worked CRM case study.
- Conceptual evaluation: the answer to "What is a critical conceptual
  evaluation of this `technical element instance`?" is judged against the
  canonical conceptuum guide
  (`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md`),
  not written freehand. Read it before writing that answer; name the concept
  and the precising definition under evaluation first; lead with the verdicts,
  then apply its `## Evaluation` criteria as a criterion → verdict → diagnostic
  table (its minimum set is Conceptual Identification, Definitional Clarity,
  Conceptual Determinacy, Internal Consistency, Representational Adequacy,
  Purpose Adequacy); cite the guide in the note's References. Architectural,
  historical, or scaling commentary is not a conceptual evaluation — it
  belongs in the decomposition, the QA, or the `Technical Evolution` branch.
- Grammar source: `bin/conform.py` fetches the guide above at
  runtime (stdlib `urllib`, no local snapshot) and validates the canonical
  two-column tables: every backticked segment names a type from the guide's
  Tabular view, no type terminates a branch, paths are unique.
- Table contract: 2 columns (`Instance Tree Path | Description`) under a
  Boundary / Stopping-rule / Identity / Verbs block. Paths split on `→`;
  backticked segments are type groupings, plain segments are instances
  typed by their nearest grouping. Every path is unique and complete from
  the root; a row is terminal when it names a concrete tool, file, config
  attribute, measured value, or named actor. A skipped spine level gets a
  vendor-neutral intermediate instance (the CRM `CRM application` pattern),
  never an exemplar.
- What-type answer: the "What technical element type does this technical
  instance belong to?" Formulation answer declares one primary type chosen
  from the philosophia Tabular view; secondary readings stay as
  `readable as …` prose (OpenAPI: Standard primary, Set reading).
- Grouping segments: children are grouped under bare type-name segments
  with their own rows, so the typing reads from the instance path itself.
  Type segments are styled `` `like this` ``; instance segments stay plain.
  Exemplars realizing their parent stay direct. No type segment terminates
  a branch.
- Verbs: a tool *implements* the standard/practice; a running
  deployment/campaign/client *realizes* it. Deployment-specific values and
  named vendors appear only in rows marked exemplar.
- Technique subtrees follow the taxonomy chain Practice → Task →
  General Technique → Operative Technique → Constitutive Technique →
  Technical Act → Technical Interface & Actuation; do not skip levels or
  hang Activities under a General Technique. (`Technical Activity` is not a
  structural type — see the note's QA on why it is excluded.)
- Multi-root decomposition is the default for multi-typed instances (one root
  per candidate type — see the "How to decompose an instance that belongs to
  multiple element types?" QA in the philosophia note). On ambiguous root
  typing, ask the user for disambiguation instead of guessing; if unanswered,
  build the default root — a primary type chosen from the philosophia Tabular
  view — and record it in the note's What-type Formulation answer (secondary
  readings as `readable as …` prose).
- Depth guidance: deep core (systems + techniques to levels 4–5), shallow
  rest (context/control/lifecycle +1). `wildfly.md` is the full-recursion
  exemplar (~2.5k rows), `openapi.md` the mid-scale one (~50 rows).
- Self-check after any table edit: instance paths unique; every backticked
  segment names a guide type; no branch-terminating type segments. Then run
  `make notes-index` (below).
- **Technical-element atlas** — `technica/atlas.html` (with the generated
  `technica/atlas.json` beside it) renders the forest: the decomposition
  tables of the technica notes merged into one typed instance tree, never
  the directory layout. The tables use the canonical
  `| Instance Tree Path | Description |` form (`→` paths, backticked type
  groupings, plain instances). The page, its companion note `atlas.md` and
  `meta/` are excluded from parsing, so the atlas never indexes itself.
  Every new instance in a decomposition table is in the forest by
  construction: regenerate the store after any table edit under
  `src/corpus/notes/technica/` with `make atlas-index` (validated by
  `make atlas-check`, part of `make check` — one synthetic root, unique
  sibling labels, sources exist, note links resolve, stats; table grammar
  conformance stays `conform.py`'s job). The page uses the same form as
  `technical-object-taxonomy.html`: one `TreeCatalog` mount over the forest
  (the left tree is the instance tree — the node id *is* the `→` path —
  opened two levels with `openDepth`, filled lazily on expand) and a
  node inspector on the right (kind/type chips, description, instance tree
  path, the notes that decompose it, `Contains` children). `?node=<path>`
  deep-links; `#<path>` is written by the shared viewer. There is no card or
  dendrogram view. The store is generated data — never hand-edit it, never
  changelog it.
- **Approximation Playground** — `epistemica/playground/approximation-playground.html`
  with its bank `approximation-problems.json` beside it. Twenty-one topics
  (estimation, division, powers & roots, log, trigonometry, exponentials,
  geometry, unit conversion, mean, median, mode, compounding, averaging, risk,
  ratio, expected value, discounting, volatility, base rates, pH & scales,
  half-life), each a single concept; a user selects several topics and the
  runner mixes them. The JSON holds the **scheme specs** — `kind`, prompt and
  steps templates, tolerance — and the page holds the **generators**, so a new
  topic is data plus a generator only if its kind is new. `make
  approximation-check` (part of `make check`) validates ids, kinds, table
  references, tolerance kinds and that every `{placeholder}` a template uses is
  one its generator supplies.
- **Technical-object taxonomy** — `technica/technical-object-taxonomy.{html,json}`
  under `src/corpus/notes/` is the *classification* of the corpus's
  technical objects, distinct from the atlas *decomposition*: four levels,
  **object domain → object kind → class → object**, where the object kind is
  the canonical guide's own technical-element type (`Producing Technical
  Element` and its four good-producer kinds, `Constitutive Technical Object`,
  the five `Production Support` kinds, `Machine`, `Production Virtual
  Technical Object`, `Production Technical System`). Every object node also
  carries its **good reading** (`good`: excludability & rivalry · durability ·
  production · use, quoting `social/good/good.md`'s classification table), an
  indicative HS heading, its atlas instance path, and its source note — the
  bridge that makes the goods ⇄ technical-object relation in `links.json`
  checkable rather than rhetorical. There is **no separate taxonomy file**:
  the classification is authored data carried in the store's **`taxonomy`
  section** (`{title, version, source, levels, count, counts, nodes}`),
  authored in the tracked archive `technica/atlas-taxonomy.json` and seeded
  from it into `atlas.json` on the first build, then carried over verbatim
  by every `make atlas-index` (the builder reads the section back before
  writing; a store without it is an error, never an empty section). The
  page and the checker read one file:
  `technical-object-taxonomy.html` fetches `atlas.json` and mounts
  `taxonomy.nodes`, the atlas page mounts `roots`. Edit
  `atlas-taxonomy.json`, then `make atlas-index`; `make object-taxonomy-check`
  (part of `make check`) validates the built section and fails when it has
  drifted from the archive — ids, the domain-root forest, level chain, kind
  and good enums, HS shape, atlas paths into the same store's forest, and
  note links. It is a live note, so no changelog log.

## On Epistemical Notes

- Before writing any note that types an epistemic
  element, read
  `https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`
  first — it owns the mandatory schema (`#` title, intro quote,
  `## Formulation` with the five questions — what is this epistemic
  instance, what epistemic element type does it belong to, is the type of
  this `epistemic element instance` unambiguous, what is the recursive
  instance decomposition, what is a critical conceptual evaluation of
  this `epistemic element instance` — and `## References`) and the
  decomposition table contract: a single `Instance Tree Path | Description`
  table; paths use `→`; type grouping segments are backticked and
  instances are Title Case; the root type is declared once and no type
  terminates a branch; composites take a `Set` suffix past depth 2;
  declare whether the branches are read as inquiry or as parsed reality. The
  guide's Arithmetic case study is the worked table reference — not the
  old 4-column entity-taxonomy form.
- The fifth formulation question — "what is a critical conceptual evaluation
  of this `epistemic element instance`?" — is answered against the same
  conceptuum guide
  (`https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md`):
  criteria table plus verdict, guide cited in References, never freehand
  commentary. Verdicts lead; the criteria table follows. Notes predating this
  rule keep their existing evaluation until it is rewritten for another reason.
- The guide is canonical at the Naturgnosis raw URL above; the former local
  copies (`src/notes/bin/epistemicarum-guide.md` and
  `src/notes/bin/epistemicarum-guideline/`) were removed when the guide was
  centralized — cite that URL in notes. The corpus lives under
  `src/corpus/notes/epistemica/` and was seeded from the Modelado Notion
  export (one-off migration; the importer was removed after use —
  mechanical normalization only, the schema conversion is still
  outstanding).
- The validation notes live in `epistemica/validation/` — `validation.md`
  (master), `probability-model-validation.md`, `calibration.md`,
  `statistical-hypothesis-testing.md`, `p-value.md`, `e-value.md`,
  `goodness-of-fit.md`, and `confidence-interval.md` (procedure-coverage
  reporting, moved out of the observational domain); calibration is a distinct
  practice, not a synonym for validation.
- The **experimental-method scope** lives in `epistemica/experimental-method/`:
  `experimental-method.md` is the scope master (`order: 0`) — the routines by
  which a system is made to yield observations, filed by what the routine does
  to the system (perturbation, stimulation, ablation, recording, imaging,
  preparation) with the access / infrastructure / evaluation lanes and one
  shared controls spine — and `optogenetics.md` is the first routine note.
  Method notes decompose the routine into sub-methods only; tools and standards
  are carried by the scope's lanes. The material side stays in `epistemica/data/`
  (collection, design, the dated cases) and the identification reading in
  `epistemica/causality/`; the same routine read as production is a technica
  `Technique`, never a second epistemica note.
- The **singular scope** lives in `epistemica/singular/`: the former
  `science/` notes together with the notes that bind one particular
  epistemic-element instance rather than a domain — `firm-clustering`,
  `firm-profiling`, `industry-analysis`, `swe-productivity`,
  `problematization`, …. The `epistemica/` root keeps the domain catalogues,
  the master `ees.md`, and the general forms such as `production-function`.
- **Terminology atlas** — `epistemica/horror/terminology.{json,html}`
  stores and renders the misnomer/legacy/false-friend inventory (statistics,
  probability, measurement); `make terminology-check` validates the store
  (part of `make check`). The page is reached through the catalog's
  `epistemica/horror/` folder, no promoted card.
- **Symbol atlas** — `epistemica/symbols.{json,html}` stores and
  renders the mathematical-notation inventory (glyph, category, description,
  origins, usage, related symbols, note links); `make symbols-check`
  validates the store (part of `make check`). The page is reached through
  the catalog's `epistemica/` root, no promoted card.
- **P-Value Atlas** — `epistemica/validation/atlas/pvalue.{json,html}` stores
  the null-distribution inventory (normal, t, chi-square, F, gamma,
  exponential, beta, uniform, Cauchy, Kolmogorov–Smirnov, binomial, Poisson,
  hypergeometric, negative binomial, geometric, multinomial, permutation,
  bootstrap, Mann–Whitney) and renders it as a **playground**: pick any law
  from the family picker, read its support/parameters/statistic/definition/
  formulas, move parameter sliders and `t_obs`, and see the density/mass with
  the tail shaded, the CDF with the tail band, and live F(t), density/mass,
  left/right/two-sided p, moments, and α decision. The Monte Carlo strip adds
  the null cloud, the p-value histogram, and analytic-vs-simulated p.
  `make pvalue-check` validates the store (part of `make check`). The page is a
  live note reached through the catalog's `epistemica/validation/atlas/`
  folder and linked from `p-value.md`, no promoted card.
- **Goodness-of-Fit Atlas** — `epistemica/validation/atlas/gof.{json,html}`
  stores the law inventory (normal, exponential, gamma, Weibull, log-normal,
  uniform, beta, Poisson, binomial) and the discrepancy measures (Pearson χ²,
  likelihood-ratio G, Kolmogorov–Smirnov, Cramér–von Mises, Anderson–Darling)
  and renders a **playground**: pick a law and a measure, set `n` and the
  contamination `δ` (the fraction of observations drawn from a distorted
  version of the law), toggle parameter estimation, and read the empirical
  CDF/PMF against the fitted model, the observed discrepancy against its null
  cloud, the power curve over `n`, and the p-value calibration histogram.
  Asymptotic nulls are used only where they hold (χ²/G and Kolmogorov with
  fixed parameters, D'Agostino–Stephens Anderson–Darling when fully specified);
  estimated parameters and Cramér–von Mises always use a resampled null.
  `make gof-check` validates the store (part of `make check`); `?selftest`
  runs the numeric cases and `?sweep` exercises every law × measure pair. The
  page is a live note reached through the catalog's
  `epistemica/validation/atlas/` folder and linked from `goodness-of-fit.md`,
  no promoted card.
- **Playgrounds** — one centralised interactive notebook surface at
  `epistemica/playground/`: `index.html` is the notebook index (one card per
  notebook, grouped under *Estimation & statistics* and *Geometry*, the book
  icon opening the corpus note and `▶ play` opening the notebook), and each
  notebook is a live page beside it. The former per-domain surfaces
  (`epistemica/observational/playground/`, `epistemica/mathematical/playground/`)
  were consolidated here. The
  playground's `principal-component-analysis.html` is a six-act narrative — the
  shadow problem, projection, the variance/reconstruction-error duality, the
  centre → covariance → eigenvector algorithm with a drag-rotatable 3-D lab, a
  64-dimensional 8×8 digit PCA with scree / 64→2 scatter / k-component
  reconstruction, and the takeaways — with every figure computed in-browser
  from a seeded cloud. The mathematical playground's
  `rotation-playground.html` turns a point, segment, or polygon about the
  origin, the figure's own centre, a vertex, or a dragged point, drawing each
  vertex's arc and the live coordinates with a theme-aware canvas. New
  notebooks add one page plus one card; live HTML is out of changelog scope,
  and a corpus note that links its notebook logs the edit like any other
  content change.
- **Mathematical Area Atlas** — `epistemica/mathematical/atlas.{json,html}`
  stores and renders the sub-discipline inventory (`Area | Essence | Family |
  Axis | Notes`), with table, family-grid, and property × operation map views,
  search dimming/highlighting, and a detail modal. `make math-atlas-check`
  validates the store (part of `make check`). The page is a live note reached
  through the catalog's `epistemica/mathematical/` folder, no promoted card.
- **Geometric Shape Atlas** — `epistemica/mathematical/geometry/atlas.{json,html}`
  renders every row of the `geometric-shape.md` decomposition table as a
  figure-first entry: an inline SVG drawing for every node, outline, family,
  and table views, family/dimension filters, search, and a detail modal with
  the source path and corpus-note links. `make shape-atlas-index` regenerates
  the store from the table (after any table edit) and `make shape-atlas-check`
  validates it (part of `make check`). The page is a live note reached through
  the catalog's `epistemica/mathematical/geometry/` folder, and
  `geometric-shape.md` links it; no promoted card.
- **EES** (`epistemica/ees.md` + `ees.html` + `ees.json`) is the master
  epistemic inventory. The tree is stored canonically in `ees.json`
  (`roots[]`; each node `{label, type, kind, order, description, children}`;
  `kind` ∈ root|grouping|instance; `order` ∈ epistemic|ontic|reflexive); the
  atlas `ees.html` renders it in two views (outline, cards) plus an element
  search and is the single place the **complete, ever-expanding decomposition**
  lives.
  The note keeps only the schema, formulation, and a branch backbone and points
  to the atlas. Validate after any tree edit with `make ees-check` (also part
  of `make check`); `ees.json` is data — only `ees.md` changes are logged in
  the changelog.

## On Natural Notes

- Notes under `src/corpus/notes/nature/` type natural elements — the
  representation of the world, observer-independent reality. Before writing
  any note there, read
  `https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md`
  first — it owns the schema (`#` title, intro quote, `## Formulation` with
  the three questions — what natural element type does this natural
  instance belong to, what is this natural instance, what is the recursive
  instance decomposition of this natural instance — and `## References`)
  and the decomposition table contract: a single 2-column
  `Instance Tree Path | Description` table whose paths begin at
  `Ontic Element`, descend through the licensed kind chain, then take one
  labelled link per step (`(→ Kind)`, `(→ Part)`, `(→ Attribute)`, … —
  a bare `→` is never allowed); grouping types are `` `code` ``, instances
  are Title Case plain text; every leaf resolves to a natural instance and
  no type terminates a branch; the root's own type is never re-expressed
  through an intermediate. Declare the level of organization
  (micro/meso/macro) on each instance row and record the Limitation
  checklist items the instance exhibits. The retired 4-column table with
  `Natural Category` and `Natural Element Type Tree Path` is not used for
  new notes.
- The guide is canonical at the Naturgnosis raw URL above — cite that URL
  in notes. The directory is created with the first note (like the other
  sections, the top-level dir is the section); run `make notes-index`
  after any corpus edit.
- `nature/bio/` is the life family, filed by **ontic kind**, never by field
  of study: `organism/` (with `virus/`, `bacteria/`, `protist/`, `fungus/`,
  `plant/`, `animal/`), `genome/`, `molecular/`, `cell/`, `ecosystem/`,
  `process/`. `bio.md` is its master and carries the kind table. There is no
  `genetics/`, `biochemistry/` or `ecology/` dir — those are epistemic
  disciplines; the corpus files the element (genome, protein, ecosystem) and
  leaves the discipline reading to `epistemica/`. `nature/human/` holds the
  human instance of the same family and is not duplicated here. Links use
  `n=nature/bio/…`.
- `nature/wave/` is the wave corpus: the wave and oscillation elements off the
  `nature/` root — the master (`wave`), the phenomena and formal notes
  (`wave-phenomena`, `wave-propagation`, `wave-equation`, `wave-speed-v`,
  `wavelength`, `wave-function`, `wave-particle-duality`, `wave-energy`), the
  specific waves (`radio-wave`, `gravitational-wave` and its detection,
  `spin-waves-magnons`, `physical-properties-of-sound-waves`) and the
  oscillation notes (`oscillating-electric-current`,
  `plasma-or-charge-separation-oscillations`, `square-wave-ac`,
  `triangular-wave-ac`). Wave *properties* and observations that are not
  themselves waves (`frequency-periodicity`, `amplitude-a`, `pitch`,
  `loudness`, `propagation-of-sound`, `interferometry`, light, photons,
  radiation) stay on the `nature/` root. Links use `n=nature/wave/…`.
- `nature/human/` is the human corpus: every natural element whose instance
  is the human being — the body (organs, organ systems, tissues, fluids), the
  physiology (metabolism, homeostasis, hormones, sleep, immunity), the senses
  and the mind (perception, attention, memory, emotion, cognition,
  behaviour), plus the `cognitive/` and `behavioral/` branches with their
  conceptual-model sets. Notes about human nature that get moved off the
  `nature/` root land here rather than being duplicated; the branch masters
  are `human`, `cognitive` and `behavioral`, and a natural note that already
  exists under `nature/` is never copied in twice. Links use
  `n=nature/human/…`.

## On Extracting Content from a Document

- When asked to extract the content of a document (a book, paper, report,
  notebook source, or corpus entry), use the canonical reading guide at
  `https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-lectionis-et-operis.md`
  — it owns the extraction schema and the table form.
- Produce the inventory as one table, one row per element, in the guide's
  columns: `Content (Epistemic, Technical, Normative) Type | Instance Path
  Tree | Description | Source (Page, Paragraph)`. Not prose, not a summary.
- Characterise each element from the guide's references rather than
  freehand: the content family selects the type vocabulary — epistemic per
  *Philosophia Artium Epistemicarum et Operis*, technical per *Artium
  Technicarum*, normative per *Socialium* / *Moralis*, concepts per
  *Conceptuum*, natural elements per *Naturalis*; Dialectic, Principle, and
  Ambiguity Resolution cover the in-between cases. Read the referenced guide
  before typing a row, and cite the lectionis guide in the extraction's
  references.
- The `Instance Path Tree` follows the owning element guide (backticked
  grouping segments, Title Case instances, no bare type terminating a
  branch); every row carries its `Source` locator — no source, no row.
- The guide is marked `unfinished`: state the edition/source artifact and
  record gaps instead of silently widening the enum (natural and conceptual
  elements are not among the three content families).
- No fixed home for extraction artifacts yet — ask before writing one into a
  corpus or under `spec/`.

## Run / Verify Locally

```
cp .env.example .env            # optional: repo-local config
make run                        # dev server on :8010 (python3 bin/serve.py --port 8010)
python3 bin/serve.py            # same server directly on :8000
```

`make help` lists all targets; `make check` runs the py_compile battery below.

Verification (no test suite exists; `make check` covers the first):

- `python3 -m py_compile bin/*.py`
- Catalog literals: `bin/check_catalog_literals.py` fails when a catalog page hardcodes a corpus entry, a directory special case, or a `data/<corpus>/…` href (part of `make check`)
- EES tree: `make ees-check` (legacy alias: `make rees-check`; validates `src/corpus/notes/epistemica/ees.json` — unique paths, no branch-terminating type segments, stats) — part of `make check`
- Technica atlas: `make atlas-index` (regenerates `src/corpus/notes/technica/atlas.json` from the canonical two-column decomposition tables of the technica corpus, the atlas page/note and `meta/` excluded — after any table edit under `src/corpus/notes/technica/`) → `make atlas-check` (one root, kinds, sibling labels, sources exist, note links resolve, stats) — part of `make check`; page `curl -s :8000/corpus/notes/technica/atlas.html` (tree + node inspector, `?node=<instance path>` deep links), reached in the catalog at the `technica/` root beside the technical-object taxonomy
- Geometric Shape Atlas: `make shape-atlas-index` (regenerates `src/corpus/notes/epistemica/mathematical/geometry/atlas.json` from the decomposition table of `geometric-shape.md`) → `make shape-atlas-check` (unique paths, family/dimension consistency, figure spec on every node, note links resolve) — part of `make check`; page `curl -s :8000/corpus/notes/epistemica/mathematical/geometry/atlas.html` (outline / families / table views, figure modal, `?view=`, `?family=`, `?dimension=`, `?q=`, and `?id=` deep links), reached in the catalog through the `epistemica/mathematical/geometry/` folder and linked from `geometric-shape.md` (no promoted card)
- Terminology crimes: `make terminology-check` (validates `src/corpus/notes/epistemica/horror/terminology.json` — unique kebab ids, enum domains/crimes/severities, resolving related ids, existing note links, well-formed sources) — part of `make check`; page `curl -s :8000/corpus/notes/epistemica/horror/terminology.html`, reached in the catalog through the `epistemica/horror/` folder (no promoted card)
- Symbol atlas: `make symbols-check` (validates `src/corpus/notes/epistemica/symbols.json` — unique ids, enum categories, non-empty symbol/description/origins/usage, resolving related ids, existing note links, well-formed sources) — part of `make check`; page `curl -s :8000/corpus/notes/epistemica/symbols.html`, reached in the catalog through the `epistemica/` root (no promoted card)
- P-Value Atlas: `make pvalue-check` (validates `src/corpus/notes/epistemica/validation/atlas/pvalue.json` — unique ids, known families/engines, complete density/CDF/left/right/two-sided formulas, parameter specs in range, resolving related ids and note links, well-formed sources) — part of `make check`; page `curl -s :8000/corpus/notes/epistemica/validation/atlas/pvalue.html` (playground-first: family picker + parameter sliders + `t_obs` + density/CDF stages + live readouts + Monte Carlo strip; `?selftest` for the numeric cases), reached in the catalog through the `epistemica/validation/atlas/` folder and linked from `p-value.md` (no promoted card)
- Goodness-of-Fit Atlas: `make gof-check` (validates `src/corpus/notes/epistemica/validation/atlas/gof.json` — unique law/measure ids, known engines, complete formulas, parameter specs in range, `m` consistent with the parameters, selftest cases referencing existing laws/measures) — part of `make check`; page `curl -s :8000/corpus/notes/epistemica/validation/atlas/gof.html` (playground-first: law + measure pickers, `n`/`δ` sliders, estimation toggle, empirical-vs-fitted, null cloud, power curve, p-value calibration; `?selftest` for the numeric cases, `?sweep` for every law × measure pair, `?law=…&measure=…&n=…&delta=…` deep links), reached in the catalog through the `epistemica/validation/atlas/` folder and linked from `goodness-of-fit.md` (no promoted card)
- Universal search: `make search-index` (build-time snapshot → gitignored `src/app/data/search-index.json`, corpus-only; rebuilt locally or at image build) → every surface's header via the shared `src/app/shared/usearch.js` (hub, docs, catalogs, viewers). Query syntax is free text plus `@tag` filters (AND across multiple tags, e.g. `@person @mathematics`); a bare `@` suggests the tag vocabulary from the loaded index. The query (text and tags) persists per tab in `sessionStorage` so it survives navigation — not in the URL, which the catalogs own. The dice button and `r` shortcut sample from the active filter, so `@person` + dice opens a random persona.
- `curl :8000/api/health` → `{"status":"ok","service":"epistecnica"}`
- Unified library index: `make library-index` (merges the three corpus indexes into gitignored `src/app/data/library-index.json`; part of `make index`) → `curl -s :8000/explorer.html`
- Index jobs: `make index` (all, chunked, dependency order) · `make index-status`
  (last known `done/total/pct` per builder, no build) · `make index-list` ·
  `make index-background`; with `make run`, `curl -s :8010/api/index/status`
  and `curl -s -X POST -d '{"builders":["notes"]}' :8010/api/index/build`
  (`202` started, `409` busy, `400` unknown builder)
- Legacy graphs: `curl -sI :8000/epistemica/` and `:8000/tecnica/` → `302` → `/corpus/notes/epistemica/ees.html`
- Notes: `curl -s :8000/corpus/notes` (catalog), `/view.html?p=notes/technica/general/pto/zsh.md` (viewer), `/corpus/notes/technica/general/cto/lib/concurrent-map.html` (live note, served as-is), `/data/notes-index.json` (generated — run `make notes-index` after any corpus edit; naming conventions + notes-vs-live-notes + tags in `src/corpus/README-notes.md`)
- EES atlas: `curl -s :8000/corpus/notes/epistemica/ees.html` (the multi-view atlas) and `/corpus/notes/epistemica/ees.json` (the canonical tree store it renders)
- Courses: `curl -s :8000/corpus/courses` (catalog), `/view.html?p=courses/version-control-basics` (course view: entry + lectures), `/view.html?p=courses/version-control-basics/01-why-version-control.md` (lecture), `/data/courses-index.json` (generated — run `make course-index` after any corpus edit; course-dir/readme + lectures + tags in `src/corpus/README-courses.md`; bulk import via `bin/course_import.py <notion-export-dir>`), `/data/changelog.courses.json` (per-file history)
- Documents: `curl -s :8000/corpus/documents` (catalog), `/view.html?p=documents/books/bertsekas-2008-introduction-probability-athena-scientific.md` (viewer), `/data/documents-index.json` (generated — run `make document-index` after any corpus edit; sections + tags in `src/corpus/README-documents.md`; bulk import via `bin/document_import.py <notion-export-dir>`), `/data/changelog.documents.json` (per-file history)
- Glossarium: `make glossarium-index` (chunked; `src/glossarium/app/data/index.json`, gitignored) → `curl -s :8000/glossarium/` (catalog), `/glossarium/?t=<slug>` (term view), `/glossarium/data/index.json` (lookup index); every note page loads `glossarium/js/glossarium-lookup.js` relatively with `data-glossarium`
- Q/A log: `make qa-index` (chunked; `src/qa/app/data/qa-index.json`, gitignored) → `curl -s :8000/qa/` (catalog) and `/qa/entry.html?id=qa-00001` (entry)
- Headless smoke: `google-chrome --headless=new --no-sandbox --virtual-time-budget=8000 --dump-dom http://localhost:8000/` and the `/docs` + `notes/` + `documents/` + `courses/` pages (check stderr for Uncaught errors)
- Image: `make build` (`docker build -t epistecnica:local .`) then run it (`make deploy-local`)

## Git — conventions & gotchas (global hooks apply to this repo)

- Every commit here runs the global git hooks configured via `core.hooksPath`:
  two pre-commit policies and a `prepare-commit-msg` message rewriter (all
  described below).
- Pre-commit authorization policy: staged files must be explicitly marked first:
  `mark-for-commit <file>...` (sets xattr `user.checkin`; deletions exempt;
  marks are cleaned post-commit). Unmarked staged files → commit rejected.
- Pre-commit annotation policy: `@FIXME @QUESTION @VERIFY` in staged source
  files block the commit; `@TODO @HACK @WORKAROUND` warn only. Markdown files
  are not inspected.
- Commit message guideline:
  `<type>(<optional scope>): <description>`, then optional body and optional
  footer. Allowed `<type>`: `feat` (new feature), `fix` (bug), `docs`, `style`
  (formatting or style-only, no behavior change), `refactor`, `test`, `chore`
  (maintenance).
- Gotcha: `prepare-commit-msg` overwrites every normal commit's message with
  the placeholder `type(<branch-or-jira-key>): message` + placeholder body +
  "Appended Information" file list. Any `-m`/`-F` message is lost — including
  on `git commit --amend -m` (`-m` makes the source `message`, which the hook
  rewrites). Messages survive only when the hook's source is `commit`:
  `git commit --amend` without `-m`/`-F`. Non-interactive workflow: commit the
  content (message gets clobbered), then set the real message via the editor
  hook point:
  `GIT_EDITOR="cp <msgfile>" git commit --amend --no-verify`
  (`cp <msgfile> <msgfile-arg>` overwrites the message file with your text;
  `--no-verify` skips the mark-for-commit re-check on the amended diff).
- Commits are SSH-signed via 1Password (`commit.gpgsign`, `op-ssh-sign`) —
  1Password must be unlocked or the commit fails. `rebase` does not sign its
  rewritten commits; after a rebase, re-sign with
  `git rebase <range> --exec 'git commit --amend --no-verify --no-edit -S'`.
- Remote may be ahead of local — `git fetch` and rebase before pushing.
- Keep this file and the subproject `AGENT.md`s current when you learn
  something durable about this repo. (The `src/epistemica/` and `src/tecnica/`
  subprojects were retired when the graphs moved to the Autoregia PKS.)

## Deploy

Push to `main` → CI builds and pushes `ghcr.io/dbremont/epistecnica:latest`.
Deploy with one of two make targets:

- `make deploy-server` — pull the GHCR image and run it (the production path;
  check the manifest digest changed before/after).
- `make deploy-local` — `docker build` the repo and run the local image
  (dev/testing).

Both targets run container `epistecnica` (`--network host`, port 8000 default
via `EPISTECNICA_PORT`, `.env` mounted read-only). This container replaces
the two old ones (`tecnica` on :8000, `epistemica` on :8010) — retire them
when switching over.

- Container crash-looping with `Address already in use` means another
  container holds the port (`docker ps -a`; `docker logs epistecnica`).

## Tooling notes

- **All scripts live in the repo-root `bin/` — centralized, never under
  `src/`.** The per-corpus `src/notes/bin/`, `src/courses/bin/`,
  `src/documents/bin/` dirs were merged into `bin/` (corpus tools renamed to
  avoid collisions: `notes_index.py`, `course_index.py`, `document_index.py`,
  `course_import.py`, `document_import.py`; checkers/conform/atlas builders
  keep their names). New scripts go in `bin/` with a corpus-qualified name;
  scripts locate their corpus via `REPO = Path(__file__).resolve().parent.parent`
  then `REPO / "src" / "<corpus>"` — not via their own directory depth.
- **Generated corpus indexes are gitignored** (`index.json`,
  `search-index.json`, technica `atlas.json`, `glossarium/app/data/index.json`,
  `qa/app/data/qa-index.json`, `index-status.json`, `index-build.lock`) —
  rebuild them with `make index` (the chunked runner; the per-builder `make
  notes-index` / `search-index` / `atlas-index` / `glossarium-index` /
  `qa-index` targets still exist) after a fresh clone or any corpus edit; the
  Dockerfile rebuilds them
  at image build so the image is self-contained. The exception is
  `src/app/data/links.json`: it is the hand-maintained support-link
  registry (an input the indexer reads, not a generated index), so it is
  tracked and must be committed with its edits.
- `rg` can fail with "JSON record exceeded 65536 bytes" on huge single-file
  HTML pages (the catalog/viewer pages and the generated `*.json` indexes).
  Scope the include pattern or use `bash` + `rg` directly.
- Everything is stdlib Python 3.12 + vanilla JS. The old dataset graph
  renderers (deck.gl tecnica viewer, Canvas2D epistemica viewer) left with the
  subprojects, and the local universal view was retired in favour of the
  Autoregia index. Vendored runtime bundles: the notes MathJax under
  `src/app/vendor/mathjax/`, d3 under `src/app/vendor/d3.min.js`
  (the technica atlas dendrogram) — third-party copies, keep names as-is.
- AI (DeepSeek) is called browser-direct in the editors; the token lives only
  in the browser. The backend has no AI endpoints and must never hold keys.
- User-facing pages must not reference backend scripts (`bin/...`,
  `python ...`) in UI strings — backend hints live in docs and server logs.
- The viewer (`view.html`; formerly `note.html`, `course.html`, `lecture.html`,
  `document.html`) are thin shells over one shared script,
  `src/app/shared/viewer.js` (included with `data-kind="note|course|
  lecture|document"`). The script owns all viewer behavior (ambient
  background, theme toggle, markdown load/render, front-matter tags + QA,
  changelog history modal, crumbs, TOC); the shell owns the page frame.
  Sections are linkable: every `h2`/`h3` gets a stable `#sec-<slug>` id and
  picking a TOC entry writes `toc-item=<slug>` into the URL
  (`view.html?p=…&toc-item=formulation`), which the viewer restores on load.
  When changing viewer behavior or DOM ids, change `viewer.js` — not the
  shells. Kind-specific config (query param, fetch URL, GitHub corpus
  prefix, crumbs style) lives in its `KINDS` table; adding a corpus means
  one table entry plus one thin shell page. The MathJax scripts stay in
  `view.html`'s head only; `viewer.js` calls `renderTeX()` when present.
