# Epistecnica — General Spec

> One combined home for the project's corpora and its guide. Status legend:
> ✅ built · 🎯 target / not yet implemented.

## 1. Vision

Epistecnica is a hub for the project's corpora — **notes**, **courses**,
**documents** — served by one combined server from one deployment, under one
guide-first entry page.

- **The guide** — the project's philosophia guides (*Artium Epistemicarum et
  Operis*, *Artium Technicarum et Operis*) are the canonical schema owners.
  Epistecnica foregrounds them and hosts the local **REES** atlas (Reality
  Epistemic Element Set, `src/note/app/data/epistemica/rees.html`) as their
  local companion.
- **The spaces** — the ontology graphs (**Epistemica**, **Tecnica**) and the
  lexical corpus (**Glossarium**) moved to the external **Naturgnosis** medium.
  The hub links to them from its index; the old local graph apps were
  retired and their URLs now **302** to the REES atlas.
- **The universal view** — one read-only graph over everything we hold (notes,
  courses, documents, REES), generated from our own corpus and served at
  `/graph/`.
- **The corpora** — local markdown, one catalog + viewer each, with a generated
  JSON index.

## 2. System architecture

```
                    ┌──────────────────────────────┐
   browser ────────►│  bin/serve.py (stdlib HTTP)  │
                    │  /             src/app/…      │
                    │  /graph/*      universal view │
                    │  /shared/*     nav search     │
                    │  /assets/*     shared images  │
                    │  /note/*       notes statics  │
                    │  /course/*     course statics │
                    │  /document/*   doc statics    │
                    └──────────────────────────────┘
```

- **The browser only talks to the server.** `bin/serve.py` is the only
  frontend-facing surface, and there is no database behind it — the
  notes-catalog pins are browser-local (`localStorage`). Everything else is
  static file serving.
- **No build step.** Python 3.12 stdlib server; vanilla JS. Vendored runtime
  bundles: the notes MathJax (`src/note/app/vendor/mathjax/`) and the
  universal-view renderer (`src/app/graph/vendor/`, deck.gl + socio-graph).

### Surfaces & endpoints (✅)

| Route | Purpose |
|-------|---------|
| `GET /` | Hub `src/app/index.html` — a flat link index over the guide, the universal view, and the corpora |
| `GET /docs` (also `/docs/`, `/docs.html`) | Site-wide documentation `src/app/docs.html` — theory + guide with live corpus stats; the only docs surface |
| `GET /graph/<path>` | Universal view from `src/app/graph/`: Graphive viewer over the graph generated from our own corpus (notes + courses + documents + REES), plus `data/universal-graph.json` + `data/universal-layout.json`; no API routes |
| `GET /shared/<path>` | Shared nav assets from `src/app/shared/`: `usearch.css` + `usearch.js`, the universal search used by every surface's header |
| `GET /assets/<path>` | Shared corpus-image store from `src/app/assets/` (every image referenced by corpus markdown) |
| `GET /epistemica/<path>`, `GET /tecnica/<path>` | **302** → `/note/data/epistemica/rees.html` (graphs moved to Naturgnosis) |
| `GET /note/<path>` | Notes surface from `src/note/app/`: catalog (`index.html`, dir browse/files + `@tag` search + pins), viewer (`note.html?n=<path>`, with a `history` modal from `data/changelog.json`), corpus (`data/**.md`), REES atlas (`data/epistemica/rees.html`), generated search index (`data/index.json`) |
| `GET /course/<path>` | Courses surface from `src/course/app/`: catalog, course view (`course.html?c=`), lecture view (`lecture.html?l=`), corpus |
| `GET /document/<path>` | Documents surface from `src/document/app/`: catalog (`index.html`), viewer (`document.html?d=`), corpus |
| `GET /glossarium/<path>` | **Not served here.** The lexical surface lives in the external Naturgnosis medium (`http://localhost:8013/glossarium/web/`); Epistecnica pages link out and the select-a-word popup loads its JS + index from there |
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
| Browser `localStorage` | Notes-catalog pins (`epistecnica.note-pins`) | the notes catalog (`src/note/app/index.html`); no server write |
| `src/note/app/data/**` | Notes corpus, live notes, REES atlas, `changelog.json` | hand-authored; index via `src/note/bin/index.py` |
| `src/course/app/**` | Courses corpus | hand-authored; index via `src/course/bin/index.py` |
| `src/document/app/**` | Documents corpus | hand-authored; index via `src/document/bin/index.py` |
| `src/app/data/search-index.json` | Universal search snapshot (corpus-only) | `bin/build_search_index.py` |
| `src/app/graph/data/universal-graph.json` + `universal-layout.json` | Universal view graph + layout (corpus + REES) | `bin/build_universal_index.py` + `bin/layout.py` |

## 4. Frontends

| Page | Renderer | Persists? |
|------|----------|-----------|
| `src/app/index.html` (hub) | Ambient Canvas2D constellation only | No |
| `src/app/docs.html` | Site documentation, live corpus stats | No |
| `src/app/graph/index.html` (universal view) | Vendored deck.gl renderer over the generated universal graph (surface filters, search, node records, deep links) | No |
| `note/index.html` (catalog) | Client-side dir browse/files + `@tag` search over generated `app/data/index.json` (`make notes-index`) | No |
| `note/note.html` (viewer) | On-the-fly markdown rendering (vendored `marked.min.js`); per-note `history` modal over `data/changelog.json` | No |
| `course/index.html`, `course.html`, `lecture.html` | Catalog + course/lecture views over `data/index.json` | No |
| `document/index.html`, `document.html` | Catalog + viewer over `data/index.json` | No |

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
- Cross-space navigation from the universal view into the Naturgnosis spaces
  when a local node and an external graph node describe the same
  practice/technique.
- Overview statistics strip (corpus counts, tags, entropies) computed
  client-side.

## 8. Method specs

- Book-to-forest epistemic extraction: [`epistemic-content-extraction.md`](epistemic-content-extraction.md) — the reusable algorithm, data contracts, quality gates, and run policy used for the Korzybski extraction.
