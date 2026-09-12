# Epistecnica

> One home for two ontologies: **Epistemica** — *Modelling and Epistemic Operationalization* — and **Tecnica** — *rendering purposeful (agentic) operation intelligible*.

Epistemica renders how we **know** (an ontology of ~122 epistemic-practice nodes as a
knowledge graph). Tecnica renders how we **act** (an ontology of ~40 technical-object
nodes across six layers). Epistecnica joins them under one index, one combined
deployment, and one set of conventions — while each subproject stays fully
self-contained.

## Layout

```
Epistecnica/
├── index.html            # The hub — entry point to both datasets (served at /)
├── bin/serve.py          # Combined server: hub + /epistemica/ + /tecnica/ + APIs
├── bin/envutil.py        # .env loader (per-dataset DB names)
├── bin/couchdb_client.py # Shared stdlib CouchDB client (same as the subprojects')
├── spec/                 # General spec + shared design system
├── epistemica/           # Self-contained subproject (app/, bin/, spec/, docs)
└── tecnica/              # Self-contained subproject (app/, bin/, spec.md, docs)
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
| `/` | Hub: dataset cards, live \|V\|/\|E\| identity strips, entry guidance |
| `/epistemica/` | Epistemica landing; `graph.html` viewer, `edit.html` editor, `view/…` extras |
| `/tecnica/` | Tecnica landing; `graph.html` viewer, `edit.html` editor |
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

1. Bootstrap CouchDB once (adapt host/port/user:pass to your `.env`):

   ```sh
   curl -X PUT http://127.0.0.1:5984/epistemica
   curl -X PUT http://127.0.0.1:5984/epistemica/_security -H 'Content-Type: application/json' -d '{}'
   curl -X PUT http://127.0.0.1:5984/tecnica
   curl -X PUT http://127.0.0.1:5984/tecnica/_security -H 'Content-Type: application/json' -d '{}'
   ```

   `_security` is cleared so the sync server can read anonymously; CORS must
   stay disabled (the CouchDB default) so the browser can never reach the DB.

2. Seed both databases (each subproject reads its own `.env` / `COUCHDB_DB`):

   ```sh
   python3 epistemica/bin/seed_couchdb.py
   python3 tecnica/bin/seed_couchdb.py
   ```

3. Precompute the layouts (rerun whenever a dataset changes):

   ```sh
   python3 epistemica/bin/layout.py
   python3 tecnica/bin/layout.py
   ```

## Run (combined)

```sh
cp .env.example .env        # fill in COUCHDB_USER / COUCHDB_PASSWORD
python3 bin/serve.py        # http://localhost:8000 (hub + both apps + APIs)
```

Editor "Backend Save URL" per dataset:

- Epistemica: `http://localhost:8000/epistemica/api/graph/save`
- Tecnica: `http://localhost:8000/tecnica/api/graph/save`

### Run a subproject standalone

Each subproject still runs exactly as it did before joining (its own `sync.py`,
its own port, its own `.env` next to it):

```sh
python3 epistemica/bin/sync.py   # serves epistemica/ on :8000 (standalone contract)
python3 tecnica/bin/sync.py      # serves tecnica/ on :8000 (standalone contract)
```

See `epistemica/README.md`, `epistemica/AGENT.md`, `tecnica/README.md`, and
`tecnica/AGENT.md` for the per-project details.

## Deployment

CI (`.github/workflows/deploy.yml`) builds one combined image on every push to
`main` and pushes it to GHCR as `ghcr.io/dbremont/epistecnica:latest`.

On the server:

```sh
./deploy-server.sh       # production: pull the GHCR image, run it
./deploy-local.sh        # dev/testing: docker build this repo, run the local image
```

Both scripts run the same container:

- One container (`epistecnica`), `--network host`, port **8000** by default
  (`EPISTECNICA_PORT=<port> ./deploy-server.sh` to override).
- The repo's `.env` is mounted read-only at `/srv/.env`.
- This replaces the two former deployments (`ghcr.io/dbremont/tecnica` on :8000
  and `ghcr.io/dbremont/epistemica` on :8010). Retire those containers on the
  server; the old repositories remain on GitHub untouched as archives.
- Don't run `deploy-server.sh` before CI publishes: compare
  `docker manifest inspect -v ghcr.io/dbremont/epistecnica:latest` digests
  before/after. `gh` CLI is not installed on the server; use the public GitHub
  API or registry digests.

## Specs & docs

- [`spec/spec.md`](spec/spec.md) — general spec: scope, system architecture, contracts, roadmap.
- [`spec/design.md`](spec/design.md) — the shared design system (tokens, typography, layout, motion).
- `epistemica/spec/` — Epistemica's spec and design notes.
- `tecnica/spec.md` — Tecnica's spec (schema, rendering pipeline, data contract).
- `AGENT.md` files — operating notes for coding agents, at the root and in each subproject.

## References

- [Philosophia Artium Technicarum et Operis](https://www.notion.so/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?source=copy_link)
- [Modelling Modelling](https://www.notion.so/Framework-334c0f5171ec803e8cfbe7f0bc02c575?source=copy_link)
- [Affirmation Space](https://www.notion.so/Affirmation-Space-336c0f5171ec80928f75ddbde09d7121?source=copy_link)
- [Algorithms](https://github.com/dbremont/algorithms)
