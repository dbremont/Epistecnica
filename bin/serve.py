#!/usr/bin/env python3
"""
Epistecnica combined server.

One stdlib HTTP server serving the local surfaces:

  /                     -> the hub (src/app/index.html)
  /docs                 -> site-wide documentation (src/app/docs.html)
  /corpus/...           -> the unified corpus (src/corpus/):
                           the catalog + global viewer + generated indexes
                           (app/), and the notes/, documents/ and courses/
                           content trees
  /glossarium/...       -> static files from src/glossarium/app/ (the lexical
                           corpus: catalog, term view, select-a-word lookup)
  /qa/...               -> static files from src/qa/app/ (the Q/A log: catalog
                           and single-entry viewer over data/qa.json)
  /shared/...           -> static files from src/app/shared/ (the nav search
                           included by every surface)
  /assets/...           -> static files from src/app/assets/ (the shared
                           corpus-image store)

The ontology graphs are no longer served here (they moved to the
Autoregia Personal Knowledge System, http://localhost:8088/pks/).
Legacy prefixes redirect:

  /epistemica/...       -> 302 /corpus/notes/epistemica/ees.html
  /tecnica/...          -> 302 /corpus/notes/epistemica/ees.html

Legacy REES paths redirect to their EES equivalents:

  /corpus/notes/epistemica/rees.* -> 302 /corpus/notes/epistemica/ees.*

and the service exposes these endpoints:

  GET  /api/health       -> liveness probe for the service
  GET  /api/index/status -> live index-build progress (see bin/index_jobs.py)
  POST /api/index/build  -> queue an index build (opt-in, see INDEX_API_ENV)

Index builds are chunked and asynchronous: the POST returns at once, the
build runs in a background thread, and the status endpoint reports
done/total/pct per builder so no page has to wait for a rebuild.

Notes-catalog pins are browser-local (localStorage); there is no pins API.

The pages fetch everything relative, so the catalog app at /corpus/
fetches data/library-index.json from src/app/data/, and the global
viewer fetches notes/, documents/ and courses/ from src/corpus/.

Usage:

    python bin/serve.py
    python bin/serve.py --port 8000
"""

import argparse
import json
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlencode

REPO = Path(__file__).resolve().parent.parent

HUB_HEALTH_ENDPOINT = "/api/health"

# Index-build API. Off by default so a public deployment cannot be pushed
# into a CPU-heavy rebuild from the internet; `make run` turns it on for dev.
INDEX_API_ENV = "EPISTECNICA_ALLOW_INDEX_API"
INDEX_STATUS_ENDPOINT = "/api/index/status"
INDEX_BUILD_ENDPOINT = "/api/index/build"

CORPUS_PREFIX = "/corpus"
CORPUS_DATA = "src/corpus"

GLOSSARIUM_PREFIX = "/glossarium"
GLOSSARIUM_MOUNT = "src/glossarium/app"

QA_PREFIX = "/qa"
QA_MOUNT = "src/qa/app"

SHARED_PREFIX = "/shared"
SHARED_MOUNT = "src/app/shared"

# Retired dataset prefixes: the local graphs moved to the Autoregia PKS, so their
# old URLs redirect to the local guide (the EES atlas).
LEGACY_REDIRECT_PREFIXES = ("/epistemica", "/tecnica")
LEGACY_REDIRECT_TARGET = "/corpus/notes/epistemica/ees.html"

# The atlas, tree store, and note were renamed from REES to EES. Keep old
# bookmarks working by redirecting the old paths to the new ones.
LEGACY_NOTE_REDIRECTS = {
    "/note/data/epistemica/rees.html": "/corpus/notes/epistemica/ees.html",
    "/note/data/epistemica/rees.json": "/corpus/notes/epistemica/ees.json",
    "/note/data/epistemica/rees.md": "/corpus/notes/epistemica/ees.md",
    "/notes/data/epistemica/rees.html": "/corpus/notes/epistemica/ees.html",
    "/notes/data/epistemica/rees.json": "/corpus/notes/epistemica/ees.json",
    "/notes/data/epistemica/rees.md": "/corpus/notes/epistemica/ees.md",
    "/corpus/notes/epistemica/rees.html": "/corpus/notes/epistemica/ees.html",
    "/corpus/notes/epistemica/rees.json": "/corpus/notes/epistemica/ees.json",
    "/corpus/notes/epistemica/rees.md": "/corpus/notes/epistemica/ees.md",
}

# The browser probes /favicon.ico at the host root whenever a page has no
# explicit icon link; only the hub and graph declare one, so route the probe
# to the real asset under img/ instead of letting it 404.
FAVICON_ENDPOINT = "/favicon.ico"
FAVICON_TARGET = "/img/favicon.ico"

class HubHandler(SimpleHTTPRequestHandler):
    """Hub statics + corpus mounts."""

    # ------------------------------------------------------------------
    # Static path remapping
    # ------------------------------------------------------------------

    def translate_path(self, path):
        """Map URL prefixes onto on-disk directories.

        /                -> <repo>/src/app/index.html (the hub)
        /docs[.html]     -> <repo>/src/app/docs.html
        /explorer.html      -> <repo>/src/app/explorer.html (directory explorer)
        /note.html       -> <repo>/src/app/note.html (global viewer)
        /corpus.css      -> <repo>/src/app/corpus.css
        /vendor/...      -> <repo>/src/app/vendor/...
        /corpus/notes/... -> <repo>/src/corpus/notes/...
        /corpus/documents/... -> <repo>/src/corpus/documents/...
        /corpus/courses/... -> <repo>/src/corpus/courses/...
        /data/...        -> <repo>/src/app/data/...
        anything else    -> <repo>/x
        """
        clean = path.split("?", 1)[0].split("#", 1)[0]

        # Site docs: /docs, /docs/, /docs.html -> src/app/docs.html.
        if clean in ("/docs", "/docs/", "/docs.html"):
            return super().translate_path("src/app/docs.html")

        # The two content views live in src/app/.
        if clean in ("/explorer.html", "/explorer", "/notes.html"):
            return super().translate_path("src/app/explorer.html")
        if clean == "/note.html":
            return super().translate_path("src/app/note.html")
        if clean in ("/tree.html", "/tree"):
            return super().translate_path("src/app/tree.html")
        if clean == "/corpus.css":
            return super().translate_path("src/app/corpus.css")
        if clean.startswith("/vendor/"):
            return super().translate_path("src/app" + clean)

        # The corpus tree is content only.
        if clean.startswith(CORPUS_PREFIX + "/"):
            rest = clean[len(CORPUS_PREFIX):]
            for folder in ("/notes", "/documents", "/courses"):
                if rest == folder or rest.startswith(folder + "/"):
                    return super().translate_path(CORPUS_DATA + rest)
            # Everything else under /corpus/ is a legacy app path; the
            # redirect handler in do_GET/_do_HEAD sends it to /explorer.html.
            return super().translate_path("src/app/explorer.html")

        # Hub-owned data (the universal search snapshot + corpus indexes):
        # /data/... -> <repo>/src/app/data/...
        if clean == "/data" or clean == "/data/":
            return super().translate_path("src/app/data/")
        if clean.startswith("/data/"):
            return super().translate_path("src/app" + clean)

        # Hub-owned assets (corpus images shared across surfaces):
        # /assets/... -> <repo>/src/app/assets/...
        if clean == "/assets" or clean == "/assets/":
            return super().translate_path("src/app/assets/")
        if clean.startswith("/assets/"):
            return super().translate_path("src/app" + clean)

        rel = None
        for prefix, mount in (
            (SHARED_PREFIX, SHARED_MOUNT),
            (GLOSSARIUM_PREFIX, GLOSSARIUM_MOUNT),
            (QA_PREFIX, QA_MOUNT),
        ):
            if clean == prefix or clean == prefix + "/":
                rel = mount + "/"
                break
            if clean.startswith(prefix + "/"):
                rel = mount + clean[len(prefix):]
                break

        if rel is None:
            rel = "src/app/index.html" if clean == "/" else clean

        return super().translate_path(rel)

    # ------------------------------------------------------------------
    # CORS (pages are same-origin; headers kept for external embeds)
    # ------------------------------------------------------------------

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS",
        )
        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type",
        )
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    # ------------------------------------------------------------------
    # GET
    # ------------------------------------------------------------------

    def do_GET(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]

        if path == HUB_HEALTH_ENDPOINT:
            self._handle_hub_health()
            return

        if path == INDEX_STATUS_ENDPOINT:
            self._handle_index_status()
            return

        if self._redirect_legacy_note(path):
            return

        for prefix in LEGACY_REDIRECT_PREFIXES:
            if path == prefix or path.startswith(prefix + "/"):
                self._redirect(LEGACY_REDIRECT_TARGET)
                return

        if path == FAVICON_ENDPOINT:
            self._redirect(FAVICON_TARGET)
            return

        super().do_GET()

    def do_HEAD(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]

        if self._redirect_legacy_note(path):
            return

        for prefix in LEGACY_REDIRECT_PREFIXES:
            if path == prefix or path.startswith(prefix + "/"):
                self._redirect(LEGACY_REDIRECT_TARGET)
                return

        if path == FAVICON_ENDPOINT:
            self._redirect(FAVICON_TARGET)
            return

        super().do_HEAD()

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]

        if path == INDEX_BUILD_ENDPOINT:
            self._handle_index_build()
            return

        self.send_error(404, "Not Found")

    # ------------------------------------------------------------------
    # Handlers
    # ------------------------------------------------------------------

    def _redirect_legacy_note(self, path):
        query = self.path.split("?", 1)[1] if "?" in self.path else ""
        params = parse_qs(query)
        suffix = ("?" + query) if query else ""

        target = LEGACY_NOTE_REDIRECTS.get(path)
        if target is not None:
            self._redirect(target + suffix)
            return True

        # Old per-corpus viewers -> the one global viewer.
        if path in ("/note/note.html", "/notes/note.html"):
            n = params.get("n", [""])[0]
            if n:
                if n == "epistemica/rees.md":
                    n = "epistemica/ees.md"
                self._redirect("/note.html?" + urlencode({"p": "notes/" + n}))
                return True

        if path in ("/document/document.html", "/documents/document.html"):
            d = params.get("d", [""])[0]
            if d:
                self._redirect("/note.html?" + urlencode({"p": "documents/" + d}))
                return True

        if path in ("/course/course.html", "/courses/course.html"):
            c = params.get("c", [""])[0]
            if c:
                self._redirect("/note.html?" + urlencode({"p": "courses/" + c + "/readme.md"}))
                return True

        if path in ("/course/lecture.html", "/courses/lecture.html"):
            l = params.get("l", [""])[0]
            if l:
                self._redirect("/note.html?" + urlencode({"p": "courses/" + l}))
                return True

        # The old corpus app URLs all point at the directory explorer.
        if path in ("/library", "/library/", "/library.html",
                    "/corpus", "/corpus/", "/corpus/index.html",
                    "/corpus/tree", "/corpus/tree/", "/corpus/tree.html"):
            self._redirect("/explorer.html" + suffix)
            return True
        if path == "/corpus/note.html":
            self._redirect("/note.html" + suffix)
            return True
        if path.startswith("/corpus/data/"):
            self._redirect("/data/" + path[len("/corpus/data/"):] + suffix)
            return True

        # Bare content-tree roots open the explorer at that subtree.
        for sub in ("notes", "documents", "courses"):
            if path == "/corpus/" + sub:
                self._redirect("/explorer.html?view=browse&dir=" + sub)
                return True

        # Old corpus roots -> the directory explorer at that subtree.
        for old, sub in (
            ("/note", "notes"), ("/notes", "notes"),
            ("/document", "documents"), ("/documents", "documents"),
            ("/course", "courses"), ("/courses", "courses"),
        ):
            if path == old or path == old + "/":
                self._redirect("/explorer.html?view=browse&dir=" + sub)
                return True

        # Old raw data paths -> the new content tree.
        for old, new in (
            ("/notes/data/", "/corpus/notes/"),
            ("/documents/documents/", "/corpus/documents/"),
            ("/courses/courses/", "/corpus/courses/"),
        ):
            if path.startswith(old):
                self._redirect(new + path[len(old):] + suffix)
                return True

        return False

    def _redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.end_headers()

    def _handle_hub_health(self):
        self._send_json({"status": "ok", "service": "epistecnica"})

    # -- index build API -------------------------------------------------

    def _index_api_enabled(self):
        return os.environ.get(INDEX_API_ENV) == "1"

    def _handle_index_status(self):
        if not self._index_api_enabled():
            self.send_error(404, "Not Found")
            return
        import index_jobs
        from indexlib import read_status

        state = read_status()
        self._send_json({
            "enabled": True,
            "busy": index_jobs.busy(),
            "job": state.get("job") or {"state": "idle"},
            "builders": state.get("builders") or {},
            "updated": state.get("updated"),
            "available": index_jobs.available(),
        })

    def _handle_index_build(self):
        if not self._index_api_enabled():
            self.send_error(404, "Not Found")
            return

        import index_jobs

        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        wanted = None
        if raw:
            try:
                payload = json.loads(raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                self._send_json({"error": "invalid JSON body"}, code=400)
                return
            if isinstance(payload, dict) and payload.get("builders"):
                wanted = payload["builders"]
                if not isinstance(wanted, list) or not all(isinstance(n, str) for n in wanted):
                    self._send_json({"error": "builders must be a list of names"}, code=400)
                    return

        have = index_jobs.available()
        unknown = [n for n in (wanted or []) if n not in have]
        if unknown:
            self._send_json({"error": "unknown builder(s): " + ", ".join(unknown),
                             "available": have}, code=400)
            return

        queued = index_jobs.expand(wanted or have)
        if not index_jobs.run(wanted):
            current = (self._last_status() or {}).get("job") or {}
            self._send_json({"status": "busy", "running": current.get("builders", [])},
                            code=409)
            return

        self._send_json({"status": "started", "builders": queued,
                         "status_url": INDEX_STATUS_ENDPOINT}, code=202)

    @staticmethod
    def _last_status():
        from indexlib import read_status
        return read_status()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _send_json(self, obj, code=200, extra_headers=None):
        body = json.dumps(obj).encode("utf-8")

        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for key, value in (extra_headers or {}).items():
            self.send_header(key, value)
        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):
        sys.stderr.write(
            "[serve] %s - %s\n" % (self.address_string(), fmt % args)
        )


def main():
    parser = argparse.ArgumentParser(
        prog="serve.py",
        description="Epistecnica combined server (hub + notes/courses/documents).",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000).",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0).",
    )

    args = parser.parse_args()

    app_dir = REPO / "src" / "app"
    if not app_dir.is_dir():
        print("ERROR: app dir not found: %s" % app_dir, file=sys.stderr)
        return 1
    corpus_data = REPO / CORPUS_DATA
    if not corpus_data.is_dir():
        print("ERROR: corpus data dir not found: %s" % corpus_data, file=sys.stderr)
        return 1
    for prefix, mount in (
        ("shared", SHARED_MOUNT),
        ("glossarium", GLOSSARIUM_MOUNT),
        ("qa", QA_MOUNT),
    ):
        app_dir = REPO / mount
        if not app_dir.is_dir():
            print("ERROR: %s static dir not found: %s" % (prefix, app_dir), file=sys.stderr)
            return 1
    hub_page = REPO / "src" / "app" / "index.html"
    if not hub_page.exists():
        print("ERROR: hub page not found: %s" % (hub_page,), file=sys.stderr)
        return 1

    handler = HubHandler

    server = HTTPServer((args.host, args.port), handler)

    display_host = "localhost" if args.host in ("0.0.0.0", "::") else args.host

    print("══════════════════════════════════════════════")
    print("  Epistecnica Server")
    print("──────────────────────────────────────────────")
    print("  Hub:     http://%s:%d/" % (display_host, args.port))
    print("  Glossary:http://%s:%d%s/" % (display_host, args.port, GLOSSARIUM_PREFIX))
    print("  Q/A:     http://%s:%d%s/" % (display_host, args.port, QA_PREFIX))
    print("  Health:  http://%s:%d%s" % (display_host, args.port, HUB_HEALTH_ENDPOINT))
    print("  Corpus:  http://%s:%d/explorer.html" % (display_host, args.port))
    print("  Docs:    http://%s:%d/docs" % (display_host, args.port))
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
