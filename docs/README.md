# Epistecnica Documentation

> One home for two ontologies: **Epistemica** — *Modelling and Epistemic Operationalization* — and **Tecnica** — *rendering purposeful (agentic) operation intelligible*.

Epistemica renders how we **know** (an ontology of ~122 epistemic-practice nodes as a
knowledge graph). Tecnica renders how we **act** (an ontology of ~40 technical-object
nodes across six layers). Epistecnica joins them under one index, one combined
deployment, and one set of conventions — while each subproject stays fully
self-contained.

## Layout

```
Epistecnica/
├── src/app/index.html    # The hub — entry point to both datasets (served at /)
├── bin/serve.py          # Combined server: hub + /epistemica/ + /tecnica/ + APIs
├── bin/envutil.py        # .env loader (per-dataset DB names)
├── bin/couchdb_client.py # Shared stdlib CouchDB client (same as the subprojects')
├── spec/                 # General spec + shared design system
├── docs/                 # Documentation hub (README mirrors this file)
├── src/note/             # Notes corpus + catalog/viewer (served at /note/)
├── src/epistemica/       # Self-contained subproject (app/, bin/, spec/, docs)
└── src/tecnica/          # Self-contained subproject (app/, bin/, spec.md, docs)
```

Each subproject keeps its own `app/` (viewer `graph.html`, editor `edit.html`,
landing `index.html`), its own `bin/` (its standalone `sync.py`, `layout.py`,
`seed_couchdb.py`), docs, and README. Nothing in a subproject depends on the
combined layer; the combined layer depends on both.

## Architecture in one paragraph

One stdlib Python server (`bin/serve.py`) serves everything. The browser talks
**only** to this server — **it never talks to CouchDB directly** (CouchDB CORS
stays disabled). One CouchDB instance hosts two databases (`epistemica`,
`tecnica`; one document per node, `_id == node.id`, plus a `layout` doc per DB).
Graph layouts are precomputed offline (`<subproject>/bin/layout.py`) and stored
in the DB `layout` doc with a static `app/data/layout.json` fallback.

## Surfaces

| URL | What |
|-----|------|
| `/` | Hub: project cards, live \|V\|/\|E\| identity strips, entry guidance |
| `/epistemica/` | Epistemica landing; `graph.html` viewer, `edit.html` editor, `about.html` + `docs.html` plates |
| `/tecnica/` | Tecnica landing; `graph.html` viewer, `edit.html` editor |
| `/note/` | Notes: searchable catalog (`index.html`), markdown viewer (`note.html?n=<path>`), corpus (`notes/**.md`) |
| `/epistemica/api/{health,nodes,layout,graph/save}` | Epistemica API (DB `epistemica`) |
| `/tecnica/api/{health,nodes,layout,graph/save}` | Tecnica API (DB `tecnica`) |
| `/api/health` | Aggregate health of both backends |

The API contract is identical to each subproject's `bin/sync.py`:
`/api/nodes` proxies CouchDB (flat array, `_id`/`_rev` stripped, layout doc
excluded, hard 502 when CouchDB is down), `/api/layout` serves the precomputed
layout (DB doc primary, file fallback, `X-Layout-Source` header), and the
editor's save URL POSTs `/api/graph/save` (proxied to CouchDB `_bulk_docs`).

## Data backend

The data backend is **CouchDB** — one instance, two databases. Connection comes
from a gitignored `.env` (copy `.env.example`).

1. Bootstrap CouchDB once — `make bootstrap` creates both DBs, clears their
   `_security`, seeds the nodes via each subproject's `bin/seed_couchdb.py`,
   and precomputes the layouts (`bin/layout.py` per dataset). Re-runnable.

   By hand, that is (adapt host/port/user:pass to your `.env`):

   ```sh
   curl -X PUT http://127.0.0.1:5984/epistemica
   curl -X PUT http://127.0.0.1:5984/epistemica/_security -H 'Content-Type: application/json' -d '{}'
   curl -X PUT http://127.0.0.1:5984/tecnica
   curl -X PUT http://127.0.0.1:5984/tecnica/_security -H 'Content-Type: application/json' -d '{}'
   python3 src/epistemica/bin/seed_couchdb.py
   python3 src/tecnica/bin/seed_couchdb.py
   python3 src/epistemica/bin/layout.py
   python3 src/tecnica/bin/layout.py
   ```

   `_security` is cleared so the sync server can read anonymously; CORS must
   stay disabled (the CouchDB default) so the browser can never reach the DB.

## Run (combined)

```sh
cp .env.example .env        # fill in COUCHDB_USER / COUCHDB_PASSWORD
make run                    # dev server on http://localhost:8010 (no docker)
python3 bin/serve.py        # same server directly, port 8000
```

`make check` runs the verification battery (py_compile all servers +
node --check the two API js files).

Editor "Backend Save URL" per dataset:

- Epistemica: `http://localhost:8000/epistemica/api/graph/save`
- Tecnica: `http://localhost:8000/tecnica/api/graph/save`

### Run a subproject standalone

Each subproject still runs exactly as it did before joining (its own `sync.py`,
its own port, its own `.env` next to it):

```sh
python3 src/epistemica/bin/sync.py   # serves src/epistemica/ on :8000 (standalone contract)
python3 src/tecnica/bin/sync.py      # serves src/tecnica/ on :8000 (standalone contract)
```

See `src/epistemica/README.md`, `src/epistemica/AGENT.md`, `src/tecnica/README.md`, and
`src/tecnica/AGENT.md` for the per-project details.

## Deployment

CI (`.github/workflows/deploy.yml`) builds one combined image on every push to
`main` and pushes it to GHCR as `ghcr.io/dbremont/epistecnica:latest`.

On the server:

```sh
make deploy-server       # production: pull the GHCR image, run it
make deploy-local        # dev/testing: docker build this repo, run the local image
```

Both targets run the same container (`make help` lists all targets):

- One container (`epistecnica`), `--network host`, port **8000** by default
  (`make deploy-server EPISTECNICA_PORT=<port>` to override; `.env`'s
  `EPISTECNICA_PORT` also applies).
- The repo's `.env` is mounted read-only at `/srv/.env`.
- This replaces the two former deployments (`ghcr.io/dbremont/tecnica` on :8000
  and `ghcr.io/dbremont/epistemica` on :8010). Retire those containers on the
  server; the old repositories remain on GitHub untouched as archives.
- Don't run `make deploy-server` before CI publishes: compare
  `docker manifest inspect -v ghcr.io/dbremont/epistecnica:latest` digests
  before/after. `gh` CLI is not installed on the server; use the public GitHub
  API or registry digests.

## Notes

The written corpus behind both ontologies lives in `src/note/app/notes/` —
plain markdown, kebab-case filenames (convention in `src/note/README.md`).
Rebuild the search index after any corpus edit:

```sh
make notes-index
```

Browse at `/note/` (catalog: search + section facets) and
`/note/note.html?n=notes/pto/zsh.md` (viewer, rendered on the fly). Markdown
files are **notes**; self-contained hand-authored HTML pages under
`notes/live/` are **live notes** — indexed and searchable, linked directly
(e.g. `/note/notes/live/chmc.html`).

## Specs & docs

- [`spec/spec.md`](spec/spec.md) — general spec: scope, system architecture, contracts, roadmap.
- [`spec/design.md`](spec/design.md) — the shared design system (tokens, typography, layout, motion).
- `src/epistemica/spec/` — Epistemica's spec and design notes.
- `src/tecnica/spec.md` — Tecnica's spec (schema, rendering pipeline, data contract).
- `AGENT.md` files — operating notes for coding agents, at the root and in each subproject.

## References

- [Philosophia Artium Technicarum et Operis](https://www.notion.so/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?source=copy_link)
- [Modelling Modelling](https://www.notion.so/Framework-334c0f5171ec803e8cfbe7f0bc02c575?source=copy_link)
- [Affirmation Space](https://www.notion.so/Affirmation-Space-336c0f5171ec80928f75ddbde09d7121?source=copy_link)
- [Algorithms](https://github.com/dbremont/algorithms)
