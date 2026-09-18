# Epistecnica — General Spec

> One combined home for two sibling ontologies and their tools. Status legend:
> ✅ built · 🎯 target / not yet implemented.

## 1. Vision

Two graphs answer two halves of one question — how do we know, and how do we
act?

- **Epistemica** — *Modelling and Epistemic Operationalization*. An ontology of
  ~122 epistemic-practice nodes (artifacts, agents, tools, constraints,
  standards) with edges in a per-node `relationships` list. Its thesis:
  epistemic practice can be rendered intelligible and systematically improved.
- **Tecnica** — *A framework for rendering purposeful (agentic) operation*. An
  ontology of ~40 technical objects across six layers (`layer` enum), edges in
  a per-node `relationship_set` (13 relation families, 45 relation types),
  with per-category conditional subschemas (`app/data/schema/schema.json`,
  JSON Schema draft 2020-12; rationale in `app/data/schema/note`).

**Epistecnica** is the umbrella: one index (the hub), one combined server, one
deployment, one set of conventions — without collapsing the two ontologies
into one. They have different schemas and different data models on purpose;
any cross-graph unification is future work, not an assumption.

## 2. System architecture

```
                    ┌──────────────────────────────┐
   browser ────────►│  bin/serve.py (stdlib HTTP)  │
                    │  /         src/app/index.html │
                    │  /epistemica/*  app statics  │
                    │  /tecnica/*     app statics  │
                    │  /note/*        notes statics│
                    │  /{ds}/api/…    CouchDB I/O  │
                    └───────────┬──────────┬───────┘
                                │          │
                    ┌───────────▼──┐  ┌────▼─────────┐
                    │ CouchDB      │  │ CouchDB      │
                    │ db epistemica│  │ db tecnica   │
                    └──────────────┘  └──────────────┘
```

- **The browser never talks to CouchDB.** The combined server is the only
  frontend-facing surface; CouchDB CORS stays disabled (default).
- **One CouchDB instance, two databases.** One document per node
  (`_id == node.id`); each DB also holds a `layout` doc
  (`{positions, computed_at, source, params}`) written by the subproject's
  `bin/layout.py`.
- **No build step.** Python 3.12 stdlib server; vanilla JS; vendored deck.gl
  (`src/tecnica/app/vendor/`); self-contained single-file HTML pages.

### Surfaces & endpoints (✅)

| Route | Purpose |
|-------|---------|
| `GET /` | Hub `src/app/index.html` (project cards, live \|V\|/\|E\| strips, entry guidance) |
| `GET /epistemica/<path>`, `GET /tecnica/<path>` | Subproject statics from `<sub>/app/` |
| `GET /note/<path>` | Notes surface from `src/note/app/`: catalog (`index.html`, search + facets), viewer (`note.html?n=<path>`), corpus (`notes/**.md`), generated search index (`data/index.json`) |
| `GET /api/health` | Aggregate health: CouchDB reachability, version, doc counts per DB |
| `GET /{ds}/api/health` | Per-dataset health (as each subproject's `sync.py`) |
| `GET /{ds}/api/nodes` | Flat JSON array; `_id`/`_rev` stripped; `layout` doc excluded; **hard 502 when CouchDB is down — no file fallback** |
| `GET /{ds}/api/layout` | `{nodeId: [x, y]}`; CouchDB `layout` doc primary, `<sub>/app/data/layout.json` fallback; `X-Layout-Source: db\|file` |
| `POST /{ds}/api/graph/save` | Body `{nodes: […], timestamp}` → `_bulk_docs` upsert, server resolves `_rev` |

where `{ds}` ∈ {`epistemica`, `tecnica`}.

### Configuration (✅)

`.env` (gitignored; see `.env.example`): `COUCHDB_URL`, `COUCHDB_USER`,
`COUCHDB_PASSWORD`, `EPISTEMICA_DB` (default `epistemica`), `TECNICA_DB`
(default `tecnica`). Real environment variables override `.env` values.
Subprojects additionally honor `COUCHDB_DB` in their standalone mode.

## 3. Data flow & ownership

| Store | Contents | Written by |
|-------|----------|------------|
| CouchDB `epistemica` | Node docs + `layout` doc | `src/epistemica/bin/seed_couchdb.py` (seed), `src/epistemica/bin/layout.py` (layout), editor saves (via server) |
| CouchDB `tecnica` | Node docs + `layout` doc | `src/tecnica/bin/seed_couchdb.py`, `src/tecnica/bin/layout.py`, editor saves |
| `<sub>/app/data/data.json` | Seed snapshot only — never the live store, never fetched by the frontend | hand-authored |
| `<sub>/app/data/layout.json` | Static layout fallback | `<sub>/bin/layout.py` |

Layouts are **precomputed** (subproject `bin/layout.py`; deterministic
Fruchterman–Reingold + phyllotaxis packing). Renderers read positions once at
load; no live force simulation. Recompute after edits is manual 🎯 (a
`/api/layout/recompute` endpoint is a future convenience).

## 4. Frontends

| Page | Renderer | Persists? |
|------|----------|-----------|
| `src/app/index.html` (hub) | Ambient Canvas2D constellation only | No |
| `epistemica/graph.html` | Canvas2D + precomputed layout (epistemica's `app/js/` shared layout code) | No |
| `epistemica/edit.html` | Canvas2D + precomputed layout, AI-assisted authoring (DeepSeek, browser-direct) | Yes (POST patch) |
| `tecnica/graph.html` | deck.gl (WebGL) + precomputed layout via `app/vendor/socio-graph.js` | No |
| `tecnica/edit.html` | deck.gl + `socio-graph.js`, AI-assisted authoring | Yes (POST patch) |
| `note/index.html` (catalog) | Client-side search over generated `app/data/index.json` (`make notes-index`) | No |
| `note/note.html` (viewer) | On-the-fly markdown rendering (vendored `marked.min.js`) | No |
| Subproject `view/…` pages | Various (stats, docs, map, note) | No |

The two renderers are intentionally independent (Canvas2D vs deck.gl); don't
unify them casually. Both editors keep the AI token in the browser only — the
backend has no AI endpoints and must never hold keys.

## 5. Deployment (✅)

- CI builds one image on push to `main`: `ghcr.io/dbremont/epistecnica:latest`.
- `make deploy-server` pulls and runs the GHCR image (production);
  `make deploy-local` builds the repo and runs the local image (dev/testing).
  Both run container `epistecnica` (`--network host`, port 8000 default via
  `EPISTECNICA_PORT`, `.env` mounted read-only).
- Replaces the two former deployments (`tecnica` :8000, `epistemica` :8010).
- Per-subproject `Dockerfile`/`deploy.sh` remain for standalone runs; CI does
  not build them.

## 6. Invariants (do not break)

1. Browser → server only; never browser → CouchDB.
2. Frontend pages fetch **relatively** (`api/…`, `data/…`) — this is what
   allows prefix mounting under `/{ds}/` without touching the huge HTML files.
3. `data.json` is a seed snapshot, not a live store; `nodes` API never falls
   back to files.
4. One subproject must not import or depend on the combined layer (or vice
   versa beyond static file serving).
5. No package managers, no frameworks, no build steps.
6. UI strings must not reference backend scripts (`bin/...`, `python ...`);
   backend hints live in docs and server logs.

## 7. Roadmap 🎯

- Cross-graph navigation from the hub (e.g. deep-link a Tecnica node from an
  Epistemica node when they describe the same practice/technique).
- Shared edge-vocabulary study: Epistemica's `relationships` families vs
  Tecnica's 13 `relationship_set` families — a mapping table before any data
  unification.
- `/api/layout/recompute` (per dataset) so edits can trigger relayout
  server-side.
- Hub-level search across both datasets (client-side over the two `nodes`
  arrays is already feasible at this scale).
- Overview statistics strip (degree distribution, components, entropies) per
  the per-project "Home Page"/"Overview" specs, computed client-side.
