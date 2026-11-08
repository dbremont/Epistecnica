# Epistecnica — General Spec

> One combined home for the project's corpora and its guide. Status legend:
> ✅ built · 🎯 target / not yet implemented.

## 1. Vision

Epistecnica is a hub for the project's corpora — **notes**, **courses**,
**documents** — served by one combined server from one deployment, under one
guide-first entry page.

- **The guide** — the project's philosophia guides (*Artium Epistemicarum et
  Operis*, *Artium Technicarum et Operis*) are the canonical schema owners.
  Epistecnica foregrounds them and hosts the local **EES** atlas (Epistemic
  Element Set, `src/corpus/notes/epistemica/ees.html`) as their
  local companion.
- **The index** — the ontology graphs and the master index live in the
  external **Autoregia Personal Knowledge System** (`http://localhost:8088/pks/`).
  The hub links to it; the old local graph apps were retired and their URLs
  now **302** to the EES atlas. The lexical corpus (**Glossarium**, at
  `/glossarium/`) and the **Q/A log** (`/qa/`) are served here again.
- **The corpora** — local markdown, one catalog + viewer each, with a generated
  JSON index.

## 2. System architecture

```
                    ┌──────────────────────────────┐
   browser ────────►│  bin/serve.py (stdlib HTTP)  │
                    │  /             src/app/…      │
                    │  /shared/*     nav search     │
                    │  /assets/*     shared images  │
                    │  /corpus/notes*       notes statics  │
                    │  /corpus/courses*     course statics │
                    │  /corpus/documents*   doc statics    │
                    └──────────────────────────────┘
```

- **The browser only talks to the server.** `bin/serve.py` is the only
  frontend-facing surface, and there is no database behind it — the
  notes-catalog pins are browser-local (`localStorage`). Everything else is
  static file serving.
- **No build step.** Python 3.12 stdlib server; vanilla JS. Vendored runtime
  bundle: the notes MathJax (`src/app/vendor/mathjax/`).

### Surfaces & endpoints (✅)

| Route | Purpose |
|-------|---------|
| `GET /` | Hub `src/app/index.html` — a flat link index over the corpora and the reference surfaces |
| `GET /docs` (also `/docs/`, `/docs.html`) | Site-wide documentation `src/app/docs.html` — theory + guide with live corpus stats; the only docs surface |
| `GET /shared/<path>` | Shared nav assets from `src/app/shared/`: `usearch.css` + `usearch.js`, the universal search used by every surface's header |
| `GET /assets/<path>` | Shared corpus-image store from `src/app/assets/` (every image referenced by corpus markdown) |
| `GET /epistemica/<path>`, `GET /tecnica/<path>` | **302** → `/corpus/notes/epistemica/ees.html` (graphs moved to the Autoregia PKS) |
| `GET /corpus/notes/epistemica/rees.{html,json,md}` | **302** → the `ees.*` equivalents (legacy REES paths) |
| `GET /corpus` (also `/explorer.html`) | Unified catalog `src/app/explorer.html`: directory browser + section tree over notes, documents and courses; search; random-document picker |
| `GET /view.html?p=<notes|documents|courses>/<path>` | One global markdown viewer for every `.md` file (course readmes also list their lectures); per-file `history` modal from the matching `data/changelog.*.json` |
| `GET /corpus/notes/<path>`, `/corpus/documents/<path>`, `/corpus/courses/<path>` | The three content trees under `src/corpus/<tree>/`, served as-is (live notes included) |
| `GET /glossarium/<path>` | Lexical surface from `src/glossarium/app/`: catalog + term view (`?t=<slug>`), generated lookup index, select-a-word popup |
| `GET /qa/<path>` | Q/A log from `src/qa/app/`: catalog + entry viewer (`?id=<qa-id>`) |
| `GET /api/health` | Liveness probe: `{"status":"ok","service":"epistecnica"}` |

The old `/{ds}/api/{health,nodes,layout,graph/save}` endpoints and their
`_bulk_docs`/`layout` semantics left with the subprojects.

### Configuration (✅)

`.env` (gitignored; see `.env.example`) carries repo-local configuration (the
deploy port). Real environment variables override `.env` values. There is no
database configuration.

## 3. Data flow & ownership

| Store | Contents | Written by |
|-------|----------|------------|
| Browser `localStorage` | Notes-catalog pins (`epistecnica.note-pins`) | the notes catalog (`src/app/explorer.html`); no server write |
| `src/corpus/notes/**` | Notes corpus, live notes, EES atlas | hand-authored; index via `bin/notes_index.py` |
| `src/corpus/documents/**` | Documents corpus | hand-authored; index via `bin/document_index.py` |
| `src/corpus/courses/**` | Courses corpus | hand-authored; index via `bin/course_index.py` |
| `src/app/data/*-index.json`, `library-index.json` | Generated per-corpus and unified indexes | `make index` (gitignored) |
| `src/app/data/changelog.*.json` | Per-corpus edit history | hand-edited, then stamped by `bin/link_changelog_commits.py` |
| `src/app/data/search-index.json` | Universal search snapshot (corpus-only) | `bin/build_search_index.py` |

## 4. Frontends

| Page | Renderer | Persists? |
|------|----------|-----------|
| `src/app/index.html` (hub) | Ambient Canvas2D constellation only | No |
| `src/app/docs.html` | Site documentation, live corpus stats | No |
| `src/app/explorer.html` (catalog) | Client-side directory browser + section tree over generated `data/library-index.json` | No |
| `src/app/view.html` (viewer) | On-the-fly markdown rendering (vendored `marked.min.js`); per-file `history` modal over `data/changelog.*.json` | No |

AI (DeepSeek) is called browser-direct in the editors; the token lives only in
the browser. The backend has no AI endpoints and must never hold keys.

## 5. Deployment (✅)

- CI builds one image on push to `main`: `ghcr.io/dbremont/epistecnica:latest`.
- `make deploy-server` pulls and runs the GHCR image (production);
  `make deploy-local` builds the repo and runs the local image (dev/testing).
  Both run container `epistecnica` (`--network host`, port 8000 default via
  `EPISTECNICA_PORT`, `.env` mounted read-only).
- Replaces the two former deployments (`tecnica` :8000, `epistemica` :8010).

## 6. Invariants (do not break)

1. Browser → server only; the server holds no database (pins are browser-local).
2. Frontend pages fetch **relatively** (`api/…`, `data/…`) — this is what
   allows prefix mounting without touching the huge HTML files.
3. No package managers, no frameworks, no build steps.
4. UI strings must not reference backend scripts (`bin/...`, `python ...`);
   backend hints live in docs and server logs.
5. User-facing pages never reference the retired subproject paths.

## 7. Roadmap 🎯

- Hub-level search across the corpora (client-side over the committed
  `search-index.json` is already feasible at this scale).
- Cross-space navigation into the Autoregia index when a local note and a
  PKS node describe the same practice/technique.
- Overview statistics strip (corpus counts, tags, entropies) computed
  client-side.

## 8. Method specs

- Book-to-forest epistemic extraction: [`epistemic-content-extraction.md`](epistemic-content-extraction.md) — the reusable algorithm, data contracts, quality gates, and run policy used for the Korzybski extraction.
