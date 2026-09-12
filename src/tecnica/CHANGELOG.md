# Changelog

All notable changes to Tecnica are documented here.
Dates are UTC; the repo has no version tags, so entries are grouped by date.

## 2026-09-03

### Architecture — the browser no longer touches CouchDB
- Added `GET /api/nodes` to `bin/sync.py`: serves the node array with `_id`/`_rev`
  stripped and the `layout` doc excluded. Hard-fails with 502 when CouchDB is
  unreachable (no file fallback — `data.json` is a seed snapshot, not the live store).
- New frontend data module `app/js/api.js` (`window.Api`: `loadNodes`, `loadLayout`)
  replaces `app/js/couch.js`; the `window.COUCHDB` direct-connection config is gone.
- API paths under `/app/api/…` are normalized to `/api/…` so dev
  (`python bin/sync.py`, default `--root .`) and prod (`--root app`) behave identically.
- Removed `bin/couchdb_setup.py`. Fresh-install bootstrap is now two manual curls
  (create the `tecnica` DB, clear its `_security` — see README); CORS on CouchDB must
  stay disabled (browser default) so the frontend can never reach the database.
- User-facing pages no longer reference backend scripts: `graph.html`'s loader error
  and console warnings were scrubbed; backend hints live in docs and server logs.

### Editor
- Manual LLM mode in AI Improve (Enhance modal): **Copy Prompt** flattens the exact
  API conversation (schema + context + node IDs + relationship-stripped node JSON +
  instructions) for pasting into any external LLM chat; **Use Pasted Result** parses
  the response back into the same diff → Apply flow. **Generate (API)** (DeepSeek)
  unchanged. Shared internals (`buildImproveMessages`, `extractJSONObject`,
  `showImprovedDiff`) guarantee both transports send/review identical content.
  `relationship_set` remains stripped and preserved in all paths.
- Fixed `loadData()` throwing `ReferenceError: layoutData is not defined` on every
  successful load (variable was block-scoped inside the `try`).
- Fixed the backend health chip: it read stale file-era fields (`data_file_exists`)
  and always showed "Backend: No data file"; it now parses the real `/api/health`
  payload and reports `Backend: Online (<n> docs)` / `Backend: DB unreachable`.

### Docs
- Added `AGENT.md` (agent-facing repo notes: architecture contract, run/verify,
  git hooks, deploy flow). Updated README, spec.md, todo.md accordingly.

## Earlier highlights (pre-changelog)

- **deck.gl (WebGL) pipeline** — viewer (`graph.html`) and editor (`edit.html`)
  migrated from Canvas2D + live force simulation to precomputed layout + vendored
  deck.gl with O(1) GPU picking and GPU-side filtering; shared renderer module
  `app/vendor/socio-graph.js`.
- **CouchDB as the data backend** — one doc per node (`_id == node.id`), layout in a
  dedicated `layout` doc; `bin/seed_couchdb.py` seeds `app/data/data.json`;
  `bin/layout.py` computes positions into both CouchDB and `app/data/layout.json`.
- **Sync server** (`bin/sync.py`) — static file serving plus `GET /api/health`,
  `GET /api/layout` (layout doc → file fallback, `X-Layout-Source` header), and
  `POST /api/graph/save` (bulk upsert, `_rev` resolved server-side).
- **Deploy** — CI builds `ghcr.io/dbremont/tecnica:latest` on every push to `main`;
  `./deploy.sh` runs the container host-networked on port 8000 with `.env` mounted.
