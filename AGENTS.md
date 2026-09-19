# AGENTS.md — notes for coding agents working in this repo

Epistecnica joins two sibling projects — `src/epistemica/` and `src/tecnica/`
— under one hub, one combined server, and one deployment. Read this file, then
the `AGENT.md` of whichever subproject you touch (`src/epistemica/AGENT.md`,
`src/tecnica/AGENT.md`); those contain per-repo details that still apply.

## What this is

- **Epistemica** — an ontology of ~122 epistemic-practice nodes as a knowledge
  graph; edges in a per-node `relationships` list.
- **Tecnica** — an ontology of ~40 technical-object nodes across six layers;
  edges in a per-node `relationship_set` list, richer per-category schema.
- **Hub** — `src/app/index.html`: entry point to both datasets, with
  live |V|/|E|/facet strips fetched from the two nodes APIs.
- No Node build step, no test suite; Python-stdlib servers in `bin/`, vanilla
  JS, vendored deck.gl (`src/*/app/vendor/`). Do not introduce package
  managers, frameworks, or build steps.

## Repo map

```
index.html              hub (served at /)
bin/serve.py            combined server — the only new surface; owns all routes below
bin/envutil.py          .env loader with per-dataset DB resolution
bin/couchdb_client.py   shared CouchDB client (byte-identical to the subprojects')
src/app/                hub page (index.html, served at /)
src/epistemica/…        subproject, self-contained (app/, bin/, spec/, AGENT.md)
src/tecnica/…           subproject, self-contained (app/, bin/, spec.md, AGENT.md)
src/note/…              notes corpus + catalog/viewer (app/ incl. app/notes/ + live notes, bin/index.py) — see src/note/README.md
src/glossarium/…        lexical corpus (terms + definitions) + catalog at /glossarium/ + select-a-word lookup on note pages — see src/glossarium/README.md
spec/                   general spec + shared design system
docs/                   documentation hub
Makefile, Dockerfile    project operations (make run/check/build/deploy-*/logs/stop) + combined image
.github/workflows/      one workflow building ghcr.io/dbremont/epistecnica
```

## Architecture contract (do not break)

**The browser never talks to CouchDB.** `bin/serve.py` is the only
frontend-facing surface in the combined deployment. CORS on CouchDB stays
disabled.

- Routes served by `bin/serve.py`:
  - `/` → hub `src/app/index.html`
  - `/docs` (also `/docs/`, `/docs.html`) → site documentation `src/app/docs.html` — the single user-facing docs surface (theory + guide, live stats from the APIs); the old per-subproject docs pages were deleted
  - `/epistemica/<path>` → static from `src/epistemica/app/<path>`
  - `/tecnica/<path>` → static from `src/tecnica/app/<path>`
  - `/note/<path>` → static from `src/note/app/<path>` (notes catalog + viewer + corpus)
  - `/glossarium/<path>` → static from `src/glossarium/app/<path>` (term catalog + corpus + lookup index); no API routes
  - `/epistemica/api/{health,nodes,layout}` and `POST …/api/graph/save` → CouchDB db `epistemica`
  - `/tecnica/api/…` (same four) → CouchDB db `tecnica`
  - `/api/health` → aggregate health for both datasets
  - `GET/POST /note/api/pins` → notes-catalog pins; single `pins` doc in
    CouchDB db `NOTES_DB` (default `notes`); POST body
    `{"path": "<note path>", "pinned": bool}`, server validates the path
    against the corpus naming rules; hard 502 when CouchDB is down
- API semantics are identical to the subprojects' `bin/sync.py`: nodes are a
  flat JSON array with `_id`/`_rev` stripped and the `layout` doc excluded;
  **hard 502 when CouchDB is down — no file fallback** (the seed `data.json`
  is a snapshot, never the live store); layout is DB-doc primary with
  `app/data/layout.json` fallback (`X-Layout-Source` header); save is proxied
  to CouchDB `_bulk_docs` with server-resolved `_rev`.
- Frontend pages fetch **relatively** (`api/…`, `data/…`) — that is what makes
  prefix mounting work without touching the huge HTML files. Keep it that way:
  never introduce absolute `/api/...` or `/data/...` paths in page code.
- Each subproject also runs standalone with its own `bin/sync.py` (its own
  contract, its own `.env`, its own port). Subproject code must not import or
  depend on the combined layer.
- DB names come from `.env`: `EPISTEMICA_DB` (default `epistemica`),
  `TECNICA_DB` (default `tecnica`), plus `COUCHDB_URL`, `COUCHDB_USER`,
  `COUCHDB_PASSWORD`. `.env` is gitignored and must stay that way.

## Run / verify locally

```
cp .env.example .env            # fill in credentials
make run                        # dev server on :8010 (python3 bin/serve.py --port 8010)
python3 bin/serve.py            # same server directly on :8000 — needs CouchDB up with both DBs
```

`make help` lists all targets; `make check` runs the py_compile + node --check
battery below.

Bootstrap (once): `make bootstrap` — creates both DBs + clears `_security`,
seeds via each subproject's `bin/seed_couchdb.py`, then runs
`<subproject>/bin/layout.py` per dataset.

Verification (no test suite exists; `make check` covers the first two):

- `python3 -m py_compile bin/*.py src/epistemica/bin/*.py src/tecnica/bin/*.py`
- `node --check src/epistemica/app/js/api.js && node --check src/tecnica/app/js/api.js`
- `curl :8000/api/health` → both datasets `couchdb_ok: true`
- `curl :8000/epistemica/api/nodes` and `/tecnica/api/nodes` → flat arrays, no `_id`/`_rev`, no layout doc
- `curl -X POST :8000/tecnica/api/graph/save -d '{"nodes":[]}'` → `{"status":"ok","saved":0}`
- Static mounts: `curl -s :8000/epistemica/graph.html | head -1` and same for `tecnica`
- Notes: `curl -s :8000/note/` (catalog), `/note/note.html?n=notes/pto/zsh.md` (viewer), `/note/notes/live/chmc.html` (live note, served as-is), `/note/data/index.json` (generated — run `make notes-index` after any corpus edit; naming conventions + notes-vs-live-notes in `src/note/README.md`)
- Glossarium: `curl -s :8000/glossarium/` (catalog; `?t=<slug>` term view), `/glossarium/data/index.json` (generated — run `make glossarium-index` after any corpus edit), `/glossarium/terms/<slug>.md` (corpus; naming + import in `src/glossarium/README.md`); note pages fetch the lookup index relatively (`../glossarium/data/index.json`) for the select-a-word popup
- Headless smoke: `google-chrome --headless=new --no-sandbox --virtual-time-budget=8000 --dump-dom http://localhost:8000/` and the two `edit.html` pages (check stderr for Uncaught errors)
- Image: `make build` (`docker build -t epistecnica:local .`) then run it against local CouchDB (`make deploy-local`)

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
  something durable about this repo.

## Deploy

Push to `main` → CI builds and pushes `ghcr.io/dbremont/epistecnica:latest`.
Deploy with one of two make targets:

- `make deploy-server` — pull the GHCR image and run it (the production path;
  check the manifest digest changed before/after).
- `make deploy-local` — `docker build` the repo and run the local image
  (dev/testing against local CouchDB).

Both targets run container `epistecnica` (`--network host`, port 8000 default
via `EPISTECNICA_PORT`, `.env` mounted read-only). This container replaces
the two old ones (`tecnica` on :8000, `epistemica` on :8010) — retire them
when switching over.

- Container crash-looping with `Address already in use` means another
  container holds the port (`docker ps -a`; `docker logs epistecnica`).
- Per-subproject `Dockerfile`/`deploy.sh` files still exist for standalone
  runs; CI does not build them.

## Tooling notes

- `rg` can fail with "JSON record exceeded 65536 bytes" on the huge single-file
  HTML pages (`edit.html` ~8k+ lines, `graph.html` ~2–4k). Scope the include
  pattern or use `bash` + `rg` directly.
- Everything is stdlib Python 3.12 + vanilla JS + vendored deck.gl. The only
  vendored runtime bundle is `src/tecnica/app/vendor/` (deck.gl +
  `socio-graph.js`); epistemica's viewer is Canvas2D with a shared `app/js/`
  layout. Don't unify the two renderers casually — they are intentionally
  independent.
- AI (DeepSeek) is called browser-direct in the editors; the token lives only
  in the browser. The backend has no AI endpoints and must never hold keys.
- User-facing pages must not reference backend scripts (`bin/...`,
  `python ...`) in UI strings — backend hints live in docs and server logs.
