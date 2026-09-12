# AGENT.md — notes for coding agents working in this repo

## What this is

Epistemica — "Modelling and Epistemic Operationalization": an ontology of ~122
epistemic-practice nodes as a knowledge graph. Read-only viewer (`app/graph.html`),
editor (`app/edit.html`) with AI-assisted authoring. No Node build step, no test
suite; Python-stdlib backend scripts in `bin/`.

## Architecture contract (do not break)

**The browser never talks to CouchDB.** `bin/sync.py` is the only frontend-facing
surface. CORS on CouchDB stays disabled.

- Frontend data access: `app/js/api.js` (`window.Api`: `loadNodes()` → `api/nodes`,
  `loadLayout()` → `api/layout`, fallback `data/layout.json`). There is no couch.js.
- `bin/sync.py` endpoints: `GET /api/health`, `GET /api/nodes` (proxies CouchDB,
  strips `_id`/`_rev`, excludes the layout doc, hard 502 — no file fallback),
  `GET /api/layout`, `POST /api/graph/save`. API paths under `/app/api/...` are
  normalized to `/api/...`.
- CouchDB db `epistemica` (see `.env`). `app/data/data.json` is the seed snapshot
  only, never fetched by the frontend. Anonymous reads are public by design; the
  sync server is the only public surface.

## Run / verify locally

```
python bin/sync.py            # needs CouchDB up; config from gitignored .env
```

`.env` keys: `COUCHDB_URL`, `COUCHDB_DB`, `COUCHDB_USER`, `COUCHDB_PASSWORD`
(gitignored; never committed).

Verification (no test suite exists):
- `python3 -m py_compile bin/*.py`
- `node --check app/js/api.js`
- `curl :8000/api/nodes` → flat JSON array, no `_id`/`_rev`, no layout doc
- Headless smoke: `google-chrome --headless=new --no-sandbox --virtual-time-budget=8000 --dump-dom http://localhost:8000/edit.html` (check stderr for Uncaught errors)

## Git — conventions & gotchas (global hooks apply to this repo)

- `core.hooksPath = ~/configs/global/git/hooks` → every commit here runs those
  global hooks.
- Pre-commit authorization policy: staged files must be explicitly marked first:
  `mark-for-commit <file>...` (sets xattr `user.checkin`; deletions exempt; marks
  are cleaned post-commit). Unmarked staged files → commit rejected.
- Pre-commit annotation policy: `@FIXME @QUESTION @VERIFY` in staged source files
  block the commit; `@TODO @HACK @WORKAROUND` warn only. Markdown files are not
  inspected.
- `prepare-commit-msg` rewrites every normal commit message to
  `type(<branch-or-jira-key>): message` + placeholder body + an "Appended
  Information" list of the committed files. All repo history looks like that;
  don't fight it.
- Commits are SSH-signed via 1Password (`commit.gpgsign`, `op-ssh-sign`) —
  1Password must be unlocked or the commit fails.
- `.env` is gitignored and must stay that way (CouchDB credentials; never committed).
- Remote may be ahead of local — `git fetch` and rebase before pushing.
- Keep `AGENT.md` current when you learn something durable about this repo.

## Deploy

Push to `main` → CI (`.github/workflows/deploy.yml`) builds and pushes
`ghcr.io/dbremont/epistemica:latest`. Then on the server run `./deploy.sh`
(pulls image, recreates the `epistemica` container: `--network host`, port 8010
by default via `EPISTEMICA_PORT`, `.env` mounted read-only).

## Tooling notes

- `rg` can fail with "JSON record exceeded 65536 bytes" on the huge single-file
  pages (edit.html is ~8.3k lines, graph.html ~2.3k); scope the include pattern
  or use `bash` + `rg` directly.
- Everything is stdlib Python 3.12 + vanilla JS + vendored deck.gl
  (`app/vendor/`); do not introduce package managers or build steps.
- AI (DeepSeek) is called browser-direct; the token lives only in the browser and
  the backend has no AI endpoints or keys. AI Improve has two transports (direct
  API / manual Copy Prompt) — keep them content-identical via
  `buildImproveMessages()`.
