# Notes

> The written corpus behind Epistecnica's ontologies — technical objects,
> external systems, libraries, operations — indexed and served at `/note/`.

## Layout

```
src/note/
├── README.md        # this document
├── bin/index.py     # search-index builder (stdlib only)
└── app/             # served statically at /note/
    ├── index.html   # catalog: search + section facets
    ├── note.html    # single-note viewer (?n=<path>)
    ├── notes.css    # markdown typography (shared design tokens)
    ├── vendor/      # vendored runtime deps (marked.min.js, alpine.min.js)
    ├── data/        # generated (index.json — do not edit)
    └── notes/       # the corpus (never machine-edited)
        └── live/    # live notes — self-contained hand-authored HTML pages
```

- Regenerate the search index after any corpus change: `make notes-index`.
- Notes are plain markdown with zero required metadata: title comes from the
  first `# ` heading (else the filename); the top-level directory is the
  section (`pto`, `cto`, `op`, …).

## Notes vs live notes

- A **note** is a markdown file (`*.md`): rendered on the fly by
  `note.html?n=<path>`. The bulk of the corpus.
- A **live note** is a self-contained, hand-authored HTML page (`*.html`),
  living under `notes/live/` — bespoke interactivity, its own scripts,
  wrapped in the shared live-note chrome (brand nav, theme toggle, footer,
  Epistecnica tokens; dark + light). Served as-is; never rendered through
  the viewer. The canonical copy-paste chrome blocks live in
  `docs/live-note-chrome.md`; no CDN libraries are allowed. The catalog
  still indexes it (title, headings, text) and links directly to the page,
  marked with a `live` chip. Examples: `live/chmc.html` ("Concurrent Map",
  from `src/tecnica/app/view/`), `live/pd.html` ("Poisson Distribution"),
  `live/hp.html` ("Hawkes Process"), `live/fpe.html` ("Fokker-Planck
  Equation"), from epistemica's former `view/tool/`.

## Pins

The catalog lets you pin notes (star button per row, `pinned` facet chip).
Pins are server-side, not per-browser: `GET/POST /note/api/pins` (served by
`bin/serve.py`) reads and upserts a single `pins` doc in the CouchDB
database named by `NOTES_DB` (default `notes`; created by `make bootstrap`).
The server validates paths against the corpus naming rules; the catalog
hides the pin UI when the API is unreachable and filters out pins whose
notes no longer exist.

## Naming convention

Note paths (directories and `.md`/`.html` filenames) must be:

- **ASCII** only — `a-z`, `0-9`, `-` (no accents, spaces, underscores, dots
  beyond the `.md`/`.html` extension)
- **lowercase** — never capitals
- **kebab-case** — words separated by `-`

Examples: `vlc-media-player.md`, `ssh-config.md`, `apache-kafka.md`,
`berkeley-packet-filter-bpf.md`. Non-markdown assets (images, code samples)
may live beside notes and are exempt from the filename rule, but directories
always follow it.

`bin/index.py` validates every note path and prints warnings for violations;
warnings never fail the build. Keep the output warning-free.
