#!/usr/bin/env python3
"""
Epistecnica combined server.

One stdlib HTTP server serving the local surfaces:

  /                     -> the hub (src/app/index.html)
  /docs                 -> site-wide documentation (src/app/docs.html)
  /graph/...            -> the universal view (src/app/graph/: Graphive viewer
                           over the graph generated from our own corpus)
  /note/...             -> static files from src/note/app/ (notes catalog,
                           viewer, corpus, generated search index)
  /course/...           -> static files from src/course/app/ (courses
                           catalog, course + lecture views, corpus,
                           generated search index)
  /document/...         -> static files from src/document/app/ (documents
                           catalog, viewer, corpus, generated search
                           index)
  /shared/...           -> static files from src/app/shared/ (the nav search
                           included by every surface)
  /assets/...           -> static files from src/app/assets/ (the shared
                           corpus-image store)

The ontology graphs are no longer served here (they moved to Naturgnosis).
Legacy prefixes redirect:

  /epistemica/...       -> 302 /note/data/epistemica/rees.html
  /tecnica/...          -> 302 /note/data/epistemica/rees.html

and the service exposes one endpoint:

  GET  /api/health      -> liveness probe for the service

Notes-catalog pins are browser-local (localStorage); there is no pins API.

The pages fetch everything relative, so corpus data (data/index.json etc.)
under /note/data/... resolves to src/note/app/data/... automatically.

Usage:

    python bin/serve.py
    python bin/serve.py --port 8000
"""

import argparse
import json
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

HUB_HEALTH_ENDPOINT = "/api/health"

NOTES_PREFIX = "/note"
NOTES_MOUNT = "src/note/app"

COURSE_PREFIX = "/course"
COURSE_MOUNT = "src/course/app"

DOCUMENT_PREFIX = "/document"
DOCUMENT_MOUNT = "src/document/app"

GRAPH_PREFIX = "/graph"
GRAPH_MOUNT = "src/app/graph"

SHARED_PREFIX = "/shared"
SHARED_MOUNT = "src/app/shared"

# Retired dataset prefixes: the local graphs moved to Naturgnosis, so their
# old URLs redirect to the local guide (the REES atlas).
LEGACY_REDIRECT_PREFIXES = ("/epistemica", "/tecnica")
LEGACY_REDIRECT_TARGET = "/note/data/epistemica/rees.html"

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

        /              -> <repo>/src/app/index.html (the hub)
        /docs[.html]   -> <repo>/src/app/docs.html (site documentation)
        /graph/x        -> <repo>/src/app/graph/x
        /note/x         -> <repo>/src/note/app/x
        /course/x       -> <repo>/src/course/app/x
        /document/x     -> <repo>/src/document/app/x
        anything else   -> <repo>/x
        """
        clean = path.split("?", 1)[0].split("#", 1)[0]

        # Site docs: /docs, /docs/, /docs.html -> src/app/docs.html.
        if clean in ("/docs", "/docs/", "/docs.html"):
            return super().translate_path("src/app/docs.html")

        # Hub-owned data (the universal search snapshot): /data/... ->
        # <repo>/src/app/data/...
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
            (GRAPH_PREFIX, GRAPH_MOUNT),
            (SHARED_PREFIX, SHARED_MOUNT),
            (NOTES_PREFIX, NOTES_MOUNT),
            (COURSE_PREFIX, COURSE_MOUNT),
            (DOCUMENT_PREFIX, DOCUMENT_MOUNT),
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
        self.send_error(404, "Not Found")

    # ------------------------------------------------------------------
    # Handlers
    # ------------------------------------------------------------------

    def _redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.end_headers()

    def _handle_hub_health(self):
        self._send_json({"status": "ok", "service": "epistecnica"})

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

    notes_app = REPO / NOTES_MOUNT
    if not notes_app.is_dir():
        print("ERROR: notes static dir not found: %s" % notes_app, file=sys.stderr)
        return 1
    for prefix, mount in (
        ("graph", GRAPH_MOUNT),
        ("shared", SHARED_MOUNT),
        ("course", COURSE_MOUNT),
        ("document", DOCUMENT_MOUNT),
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
    print("  Graph:   http://%s:%d%s/" % (display_host, args.port, GRAPH_PREFIX))
    print("  Health:  http://%s:%d%s" % (display_host, args.port, HUB_HEALTH_ENDPOINT))
    print("  Notes:   http://%s:%d%s/" % (display_host, args.port, NOTES_PREFIX))
    print("  Courses: http://%s:%d%s/" % (display_host, args.port, COURSE_PREFIX))
    print("  Docs:    http://%s:%d%s/" % (display_host, args.port, DOCUMENT_PREFIX))
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
