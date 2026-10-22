# Epistecnica Documentation

> One hub for the project's corpora — **notes**, **courses**, **documents** — under one guide-first entry page.

The project's philosophia guides — *Artium Epistemicarum et Operis* and
*Artium Technicarum et Operis* — are the canonical schema owners. Epistecnica
foregrounds them, hosts the local **REES** atlas (Reality Epistemic Element
Set) as their local companion, and serves the written corpora: notes, courses,
and documents, each a catalog + viewer over a local markdown corpus with a
generated JSON index.

The ontology graphs (**Epistemica**, **Tecnica**) no longer live here: they
moved to the external **Naturgnosis** medium. The hub links to them from its
index, and adds a **universal view** (`/graph/`) — one read-only graph
over our own corpus (notes, courses, documents, REES).

## Layout

```
Epistecnica/
├── src/app/index.html    # The hub — guide-first entry page (served at /)
├── src/app/docs.html     # Site documentation (served at /docs)
├── src/app/graph/        # Universal view (served at /graph/) — Graphive over our corpus
├── bin/serve.py          # Combined server: hub + /graph/ + /note/ + /course/ + /document/
├── bin/build_universal_index.py  # Universal-view graph builder (our corpus → graph JSON)
├── bin/layout.py         # Universal-view layout pre-computer (sunflower + FR)
├── bin/envutil.py        # .env loader
├── spec/                 # General spec + shared design system
├── docs/                 # Documentation hub (README mirrors this file)
├── src/note/             # Notes corpus + catalog/viewer (served at /note/)
├── src/course/           # Courses corpus + catalog/views (served at /course/)
└── src/document/         # Documents corpus + catalog/viewer (served at /document/)
```

## Architecture in one paragraph

One stdlib Python server (`bin/serve.py`) serves everything. There is no
database behind it: the browser only talks to this server, and the
notes-catalog pins live in the browser (`localStorage`). The old `/{ds}/api/*`
graph endpoints, their `layout` docs, and the offline layout/seed scripts left
with the subprojects.

## Surfaces

| URL | What |
|-----|------|
| `/` | Hub: a flat link index over the guide, the universal view, and the corpora |
| `/docs` | Site documentation (this content, rendered) |
| `/graph/` | Universal view: one read-only graph over notes + courses + documents + REES, generated from our corpus |
| `/note/` | Notes: searchable catalog (`index.html`), markdown viewer (`note.html?n=<path>`), corpus (`data/**.md`) |
| `/note/data/epistemica/rees.html` | The REES atlas (local companion to the guide) |
| `/course/` | Courses catalog, course view (`course.html?c=`), lecture view (`lecture.html?l=`) |
| `/document/` | Documents catalog (`index.html`) + viewer (`document.html?d=`) |
| `/epistemica/`, `/tecnica/` | **302** → `/note/data/epistemica/rees.html` (graphs moved to Naturgnosis) |
| `/api/health` | Liveness probe for the service |

## Data backend

None — every surface is static file serving, and the notes-catalog pins are
browser-local (`localStorage`), so the deployment needs no database. `.env`
(gitignored; copy `.env.example`) only carries repo-local configuration (the
deploy port).

## Run

```sh
cp .env.example .env        # optional: repo-local config
make run                    # dev server on http://localhost:8010 (no docker)
python3 bin/serve.py        # same server directly, port 8000
```

`make check` runs the verification battery (py_compile all servers + index
builders).

## External spaces

The ontology graphs and the lexical corpus are served by Naturgnosis:

- Epistemica space — `http://localhost:8011/epistemica/`
- Technique space — `http://localhost:8011/technique/`
- Glossarium — `http://localhost:8013/glossarium/web/`

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

The written corpus lives in `src/note/app/data/` — plain markdown, kebab-case
filenames (convention in `src/note/README.md`). Rebuild the search index after
any corpus edit:

```sh
make notes-index
```

Browse at `/note/` (catalog: search + section facets) and
`/note/note.html?n=technica/pto/zsh.md` (viewer, rendered on the fly). Markdown
files are **notes**; self-contained hand-authored HTML pages are **live notes**
— indexed and searchable, linked directly and co-located with their companion
note (e.g. `/note/data/technica/cto/lib/concurrent-map.html`). Live notes use
the same viewer frame and philosophia shell as regular notes (recipe in
`docs/live-note-chrome.md` §7–§8).

## Specs & docs

- [`spec/spec.md`](spec/spec.md) — general spec: scope, system architecture, contracts, roadmap.
- [`spec/design.md`](spec/design.md) — the shared design system (tokens, typography, layout, motion).
- `AGENTS.md` — operating notes for coding agents.

## References

- [Philosophia Artium Technicarum et Operis](https://www.notion.so/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?source=copy_link)
- [Modelling Modelling](https://www.notion.so/Framework-334c0f5171ec803e8cfbe7f0bc02c575?source=copy_link)
- [Affirmation Space](https://www.notion.so/Affirmation-Space-336c0f5171ec80928f75ddbde09d7121?source=copy_link)
- [Algorithms](https://github.com/dbremont/algorithms)
