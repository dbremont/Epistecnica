# Guideline

Repository conventions for Naturgnosis. Binding for all contributors and agents; global commit hooks
(`~/configs/global/git`) enforce the commit rules. Workflow guides that are large enough to stand
alone live beside this file: the [topic placement strategy](topic_placement.md), the
[nature task route](task_routing_nature.md), and the [ambiguity reading](ambiguity_resolution.md).

## File Naming

> Semantic name, semantic path, semantic URL. Lowercase, ASCII, `_` separates words.

Rules for files and directories we author:

- **Lowercase ASCII only** — no uppercase, spaces, parentheses, or diacritics in file or directory
  names.
- **`_` separates words** — `deploy_server.sh`, `seed_couchdb.py`, `aceleradoras_cientificas.md`.
- **Semantic names** — the name should say what the thing is (`seed_couchdb.py`, not `s.py`).
- **Extensions lowercase** — always `.md`, `.py`, `.sh`, `.json`, `.html`, `.png`.
- **Content slugs** — long-form notes (`app/note/data/`, the corpus home) are named after
  their content,
  slugified by the Epistecnica rule (`bin/build_note_index.py:slugify_segment()` —
  never `bin/slugify_files.py`, which emits `_`). The
  canonical human term lives inside the file (H1), never in the file name.

### Exemptions

- **Canonical tool names** — convention wins and cannot be changed: `Dockerfile`, `Makefile`,
  `docker-compose.yml`, `README.md`, `LICENSE`, `AGENTS.md`, `.gitignore`,
  `.dockerignore`, `.github/workflows/deploy.yml`.
- **This directory** — `guideline/` holds the binding conventions (this file included);
  its files follow the `_` rule above, except this entry point (`README.md`, the
  directory-entry convention shared with `spec/README.md` and `deploy/README.md`).
- **`app/*/import/`** — raw third-party exports are archival; never rename or edit (provenance).
- **`app/note/data/`** — the note corpus lives here (`<section>/<kebab-case>.md`,
  plus the generated `index.json` beside it — never hand-edit the index, rebuild with
  `make notes-index`). Corpus paths follow the Epistecnica slug rule, not the `_`
  rule above: lowercase, fixed transliterations for `æ→ae`, `ø→o`, `œ→oe`,
  `ß→ss` (no NFKD decomposition), then NFKD-normalize to ASCII, every run of
  non-alphanumeric characters becomes a single `-`, trim leading/trailing
  `-` (`my-note.md`).
   Collisions get a `-2`, `-3`, … suffix. Never run `bin/slugify_files.py`
   (which emits `_`) on the corpus; see `spec/note/authoring.md` and
  `bin/build_note_index.py:slugify_segment()` for the canonical form. The viewer
  resolves `note.html?n=<path>` against this directory. Fixed-name support files
  (`links.json`, `pins.json`, `changelog.json`, `index.json`) are exempt from
  the slug rule; they are never notes.
- **Country-keyed path segments** — where a directory is keyed by country (for
  example `app/note/data/social/actor/public/research/<code>/` or
  `app/note/data/social/actor/public/polity/<code>/region/`), use ISO 3166-1 alpha-3,
  lowercase (`usa`, `deu`, `chn`, `gbr`, `grc`); never alpha-2 or country names.
  Entities without an alpha-3 code (devolved nations, defunct states) are
  explicit exceptions.
- **`app/*/web/vendor/`** — third-party code keeps its upstream name.

## Paths & URLs

- URLs mirror paths; both are semantic: module directory = URL segment = dataset id
   (`/social/`, `/production/`, `/research/`, `/nation/`, `/technique/`, `/epistemica/`, `/note/`).
- Fixed data file names inside a module: `data.json` (dataset mirror/seed), `layout.json`
  (precomputed layout), `index.json` (generated search index), `schema.json` + `notes`
  (schema context).
- Module directories, dataset ids, and CouchDB doc keys are one and the same string; renaming one
  renames all three (breaking change — ask first).

## Derived views

A space that is a *role-based cut* over another space's nodes is a derived view, not a
dataset: it stores no nodes of its own. (First instance: Production Space is computed from
Social Space; see `app/production/AGENTS.md`.)

- **Single home**: every node lives in exactly one owning dataset. Other spaces never
  duplicate it — they compute views over it.
- **Role tags**: membership in a view is marked on the owning node with a reserved tag of
  the form `<space>-view` (today: `production-view`). The tag is exact-match (case- and
  whitespace-insensitive); ad-hoc lookalikes (`production`, `production chain`) do not
  count. When adding a node that plays a view's role, tag it in the owning editor at
  creation time.
- **Builders**: one script per view (`bin/build_<space>_view.py`, stdlib only) reads the
  owning mirror(s) and writes committed `view.json` + `view-layout.json` into the view
  module's `data/` — never `data.json`/`layout.json` (those names would resurrect the
  module as an editable dataset). Regenerate deliberately (`make <space>-view`); the files
  are committed, like the search index. Only edges with both ends in the view are kept.
- **Viewers**: the view explorer fetches `view.json`; there is no editor (edit in the
  owning space). New views follow this shape; do not invent a second mechanism.

## Commits & branches

Mirrors `~/configs/global/git/guideline.md`:

```text
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

Allowed `<type>`:

- `feat` — add a new feature
- `fix` — fix a bug
- `docs` — documentation changes
- `style` — formatting or style-only changes; no behavior change
- `refactor` — restructure code without changing behavior
- `test` — add or modify tests
- `chore` — maintenance or other changes that don't affect production behavior

Scope, when used, is the module or concern: `feat(nation): …`, `fix(sync): …`.

- `main` is the default and deployment branch.
- Working branches: `<type>/<slug>` — lowercase ASCII with `-` word separation
  (e.g. `feat/nation-index`, `fix/sync-mirror`).

## Task guides

How-to workflows for decomposition and content work. The philosophiae live as meta notes in the
corpus; the ambiguity reading lives beside these conventions.

- Technique content — `app/note/data/meta/philosophia-artium-technicarum-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-artium-technicarum-et-operis.md)):
  "How to decompose any technical instance?", single recursive table
  (`(root) := <<Technical Element>>`, system/practice/evaluation spines),
  multi-type (multi-root forest) rule, CRM case study, technical-element note schema.
- Epistemic content — `app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)):
  "How to decompose any epistemic instance?", single recursive table
  (two orders, `Epistemic Order` and `Ontic Order`, declared in the formulation), epistemic-element note schema. Form reference for all four.
- Social content — `app/note/data/meta/philosophia-socialium-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-socialium-et-operis.md)):
   "How to decompose any social instance?", single recursive table
   (`(root) := <<Social Element>>`, agentic/normative spines,
   primitive/derivative levels, Ontic/Synontic/Noetic/Multi layer catalogs,
   expanded facets with a subcategory axis),
   layer test (Ontic/Synontic/Noetic/Multi), facet assignment, social-element note schema.
- Natural content — `app/note/data/meta/philosophia-naturalis-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-naturalis-et-operis.md)):
  "How to decompose any natural instance?", single recursive table
  (`(root) := <<Natural Element>>`, composition/manifestation spines),
  level of organization, Limitation checklist, natural-element note schema. Presupposes
  the epistemicarum definitions; restates nothing from it.
- Concept content — `app/note/data/meta/philosophia-conceptuum-et-operis.md`
  ([viewer](/note/note.html?n=meta/philosophia-conceptuum-et-operis.md)):
  "Philosophia Conceptuum et Operis", the concept of a concept — formulation, ontology,
  theories of concepts, concept space, evaluation criteria, and the definition taxonomy.
  Reflective companion; states no instance-decomposition workflow.
- Ambiguity reading — `guideline/ambiguity_resolution.md`: techniques with epistemic
  goals (canonical case: well logging) and multi-root notes (canonical case:
  retail supply–demand matching, primary technical); type the means technically
  and the end epistemically, one tree per confirmed reading — and one tree per
  space in a single multi-root note — never two types on one row.
- Mathematical decomposition — `guideline/mathematical_decomposition.md`:
  content/vehicle sorting for mathematical instances (content to `Epistemic
  Construction`, vehicle to `Constitutive Substrate`, duals split not merged);
  first full application is the Arithmetic case study.

Follow the applicable workflow before decomposing instances or documenting elements; when
the root typing is ambiguous, ask the user instead of guessing.
