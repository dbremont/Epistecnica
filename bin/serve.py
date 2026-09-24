#!/usr/bin/env python3
"""
Epistecnica combined sync server.

One stdlib HTTP server serving three surfaces (the browser never talks to
CouchDB directly; CORS on CouchDB stays disabled):

  /                     -> the hub (src/app/index.html)
  /docs                 -> site-wide documentation (src/app/docs.html)
  /epistemica/...       -> static files from src/epistemica/app/
  /tecnica/...          -> static files from src/tecnica/app/
   /note/...             -> static files from src/note/app/ (notes catalog,
                            viewer, corpus, generated search index)
   /course/...           -> static files from src/course/app/ (courses
                            catalog, course + lecture views, corpus,
                            generated search index)
   /document/...         -> static files from src/document/app/ (documents
                            catalog, viewer, corpus, generated search
                            index)
   /persona/...           -> static files from src/persona/app/ (personas
                            catalog, viewer, corpus, generated search
                            index)
  /glossarium/...       -> static files from src/glossarium/app/ (lexical
                           corpus: catalog, terms, generated lookup index)

and, per dataset prefix, the same API contract as the per-project
bin/sync.py scripts:

  GET  /{ds}/api/health        -> pings CouchDB, reports db + doc count
  GET  /{ds}/api/nodes         -> flat JSON array (proxied from CouchDB;
                                  _id/_rev stripped, layout doc excluded;
                                  hard 502 when CouchDB is down)
  GET  /{ds}/api/layout         -> precomputed positions from the CouchDB
                                  'layout' doc, app/data/layout.json as
                                  fallback (X-Layout-Source header)
  POST /{ds}/api/graph/save    -> upserts {nodes, timestamp} via _bulk_docs
  GET  /api/health             -> aggregate health for both datasets

and, for the notes catalog, one preference API (server-side pins):

  GET  /note/api/pins          -> {"pins": [...]} pinned note paths
                                  (single 'pins' doc in the NOTES_DB db,
                                  default 'notes'; hard 502 when CouchDB
                                  is down)
  POST /note/api/pins          -> body {"path": "<note path>", "pinned":
                                  true|false}; validates the path against
                                  the corpus naming rules, upserts the doc

The pages fetch everything relative, so app data (data/layout.json etc.)
under /{ds}/data/... resolves to src/{ds}/app/data/... automatically.

Usage:

    python bin/serve.py
    python bin/serve.py --port 8000
"""

import argparse
import json
import re
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import couchdb_client  # noqa: E402
import envutil  # noqa: E402

REPO = Path(__file__).resolve().parent.parent

HUB_HEALTH_ENDPOINT = "/api/health"
LAYOUT_DOC_ID = "layout"

NOTES_PREFIX = "/note"
NOTES_MOUNT = "src/note/app"
NOTES_PINS_ENDPOINT = NOTES_PREFIX + "/api/pins"
PINS_DOC_ID = "pins"

COURSE_PREFIX = "/course"
COURSE_MOUNT = "src/course/app"

DOCUMENT_PREFIX = "/document"
DOCUMENT_MOUNT = "src/document/app"

PERSONA_PREFIX = "/persona"
PERSONA_MOUNT = "src/persona/app"

GLOSSARIUM_PREFIX = "/glossarium"
GLOSSARIUM_MOUNT = "src/glossarium/app"

# Note path segments follow the corpus naming rule: ASCII lowercase
# kebab-case (src/note/README.md). The last segment additionally ends .md.
NOTE_SEGMENT_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class Dataset:
    """One mounted subproject: URL prefix, static dir, CouchDB config."""

    def __init__(self, name, prefix, app_dir, layout_file, cfg):
        self.name = name
        self.prefix = prefix            # URL prefix, e.g. "/epistemica"
        self.app_dir = app_dir          # Path to src/<name>/app
        self.layout_file = layout_file  # Path to src/<name>/app/data/layout.json
        self.cfg = cfg
        self.api_base = prefix + "/api"
        # URL prefix -> on-disk mount (repo-relative logical path).
        self.mount = app_dir.resolve().relative_to(REPO).as_posix()

    def endpoint(self, api_path):
        """'/epistemica/api/nodes' -> '/api/nodes' for this dataset."""
        return api_path[len(self.api_base):]

    def matches_api(self, api_path):
        return api_path.startswith(self.api_base + "/") or api_path == self.api_base


def build_datasets():
    return [
        Dataset(
            name="epistemica",
            prefix="/epistemica",
            app_dir=REPO / "src" / "epistemica" / "app",
            layout_file=REPO / "src" / "epistemica" / "app" / "data" / "layout.json",
            cfg=envutil.dataset("EPISTEMICA_DB", "epistemica"),
        ),
        Dataset(
            name="tecnica",
            prefix="/tecnica",
            app_dir=REPO / "src" / "tecnica" / "app",
            layout_file=REPO / "src" / "tecnica" / "app" / "data" / "layout.json",
            cfg=envutil.dataset("TECNICA_DB", "tecnica"),
        ),
    ]


class HubHandler(SimpleHTTPRequestHandler):
    """Hub statics + prefix-mounted subproject statics + per-dataset API."""

    def __init__(self, *args, datasets=None, notes_cfg=None, **kwargs):
        self.datasets = datasets or []
        self.notes_cfg = notes_cfg
        super().__init__(*args, **kwargs)

    # ------------------------------------------------------------------
    # Static path remapping
    # ------------------------------------------------------------------

    def translate_path(self, path):
        """Map URL prefixes onto on-disk directories.

        /              -> <repo>/src/app/index.html (the hub)
        /docs[.html]   -> <repo>/src/app/docs.html (site documentation)
        /epistemica    -> <repo>/src/epistemica/app/ (its landing index.html)
        /epistemica/x  -> <repo>/src/epistemica/app/x
        /tecnica/x      -> <repo>/src/tecnica/app/x
        /note/x         -> <repo>/src/note/app/x
        /course/x       -> <repo>/src/course/app/x
        /document/x     -> <repo>/src/document/app/x
        /persona/x      -> <repo>/src/persona/app/x
        /glossarium/x   -> <repo>/src/glossarium/app/x
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

        rel = None
        for prefix, mount in (
            (NOTES_PREFIX, NOTES_MOUNT),
            (COURSE_PREFIX, COURSE_MOUNT),
            (DOCUMENT_PREFIX, DOCUMENT_MOUNT),
            (PERSONA_PREFIX, PERSONA_MOUNT),
            (GLOSSARIUM_PREFIX, GLOSSARIUM_MOUNT),
        ):
            if clean == prefix or clean == prefix + "/":
                rel = mount + "/"
                break
            if clean.startswith(prefix + "/"):
                rel = mount + clean[len(prefix):]
                break

        if rel is None:
            for ds in self.datasets:
                if clean == ds.prefix or clean == ds.prefix + "/":
                    rel = ds.mount + "/"
                    break
                if clean.startswith(ds.prefix + "/"):
                    rel = ds.mount + clean[len(ds.prefix):]
                    break
            else:
                rel = "src/app/index.html" if clean == "/" else clean

        return super().translate_path(rel)

    # ------------------------------------------------------------------
    # CORS (same contract as the per-project sync servers)
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

        if path == NOTES_PINS_ENDPOINT:
            self._handle_pins_get()
            return

        for ds in self.datasets:
            if ds.matches_api(path):
                endpoint = ds.endpoint(path)
                if endpoint == "/health":
                    self._handle_health(ds)
                elif endpoint == "/nodes":
                    self._handle_nodes(ds)
                elif endpoint == "/layout":
                    self._handle_layout(ds)
                else:
                    self.send_error(404, "Not Found")
                return

        super().do_GET()

    # ------------------------------------------------------------------
    # POST
    # ------------------------------------------------------------------

    def do_POST(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]

        if path == NOTES_PINS_ENDPOINT:
            self._handle_pins_post()
            return

        for ds in self.datasets:
            if ds.matches_api(path):
                endpoint = ds.endpoint(path)
                if endpoint == "/graph/save":
                    self._handle_save(ds)
                else:
                    self.send_error(404, "Not Found")
                return

        self.send_error(404, "Not Found")

    # ------------------------------------------------------------------
    # Handlers (same semantics as the per-project bin/sync.py)
    # ------------------------------------------------------------------

    def _couch_ping(self, ds):
        client = couchdb_client.Client(ds.cfg)
        couch_ok = False
        version = None
        try:
            status, body = client.get(ds.cfg.url + "/")
            couch_ok = status == 200
            if isinstance(body, dict):
                version = body.get("version")
        except Exception as exc:
            version = "error: %s" % exc

        doc_count = None
        try:
            status, body = client.get(ds.cfg.db_url)
            if status == 200 and isinstance(body, dict):
                doc_count = body.get("doc_count")
        except Exception:
            pass

        return {
            "couchdb_ok": couch_ok,
            "couchdb_version": version,
            "database": ds.cfg.db,
            "doc_count": doc_count,
        }

    def _handle_hub_health(self):
        report = {"status": "ok", "service": "epistecnica-hub", "datasets": {}}
        all_ok = True
        for ds in self.datasets:
            info = self._couch_ping(ds)
            info["status"] = "ok" if info["couchdb_ok"] else "degraded"
            all_ok = all_ok and info["couchdb_ok"]
            report["datasets"][ds.name] = info
        report["status"] = "ok" if all_ok else "degraded"
        self._send_json(report)

    def _handle_health(self, ds):
        info = self._couch_ping(ds)
        info.update(
            {
                "status": "ok" if info["couchdb_ok"] else "degraded",
                "service": "%s-sync" % ds.name,
                "couchdb_url": ds.cfg.url,
            }
        )
        self._send_json(info)

    def _handle_nodes(self, ds):
        """
        Flat JSON array of nodes: every non-design doc, the layout doc
        excluded, _id/_rev stripped. Hard 502 when CouchDB is unavailable —
        deliberately no file fallback (the seed data.json is a snapshot,
        not the live store).
        """
        try:
            docs = couchdb_client.all_docs(ds.cfg)
        except Exception as exc:
            self._send_json(
                {"status": "error", "message": "CouchDB unavailable: %s" % exc},
                502,
            )
            return

        nodes = []
        for doc in docs:
            if not isinstance(doc, dict):
                continue
            if doc.get("_id") == LAYOUT_DOC_ID or doc.get("type") == "layout":
                continue
            nodes.append(
                {k: v for k, v in doc.items() if k not in ("_id", "_rev")}
            )

        self._send_json(nodes)

    def _handle_layout(self, ds):
        """
        Precomputed layout: CouchDB doc _id 'layout' primary, static
        layout file fallback; X-Layout-Source says which.
        """
        try:
            client = couchdb_client.Client(ds.cfg)
            status, doc = client.get(ds.cfg.db_url + "/" + LAYOUT_DOC_ID)
            positions = doc.get("positions") if (
                status == 200 and isinstance(doc, dict)
            ) else None
            if isinstance(positions, dict) and positions:
                self._send_json(positions, extra_headers={"X-Layout-Source": "db"})
                return
        except Exception:
            pass

        try:
            payload = json.loads(ds.layout_file.read_text(encoding="utf-8"))
            if isinstance(payload, dict) and payload:
                self._send_json(payload, extra_headers={"X-Layout-Source": "file"})
                return
        except Exception:
            pass

        self._send_json(
            {
                "status": "error",
                "message": "layout unavailable (CouchDB doc %r unreadable and %s"
                           " missing; run python %s/bin/layout.py)"
                           % (LAYOUT_DOC_ID, ds.layout_file, ds.name),
            },
            404,
        )

    def _handle_save(self, ds):
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b"{}"

            patch = json.loads(raw)
            changed = patch.get("nodes", [])

            if not changed:
                self._send_json({"status": "ok", "saved": 0})
                return

            result = couchdb_client.bulk_upsert(changed, ds.cfg)

            self._send_json(
                {
                    "status": "ok",
                    "saved": result["ok"],
                    "new": result["new"],
                    "updated": result["updated"],
                    "errors": result["errors"],
                    "timestamp": patch.get("timestamp", ""),
                }
            )

        except couchdb_client.CouchError as exc:
            self._send_json({"status": "error", "message": str(exc)}, 502)

        except json.JSONDecodeError as exc:
            self._send_json(
                {"status": "error", "message": "Invalid JSON: %s" % exc}, 400
            )

        except Exception as exc:
            self._send_json({"status": "error", "message": str(exc)}, 500)

    # ------------------------------------------------------------------
    # Notes pins (server-side catalog preferences; CouchDB-backed)
    # ------------------------------------------------------------------

    def _valid_note_path(self, p):
        if not isinstance(p, str) or not p or len(p) > 200:
            return False
        if not p.endswith(".md"):
            return False
        parts = p.split("/")
        for i, part in enumerate(parts):
            seg = part[:-3] if i == len(parts) - 1 else part
            if not NOTE_SEGMENT_RE.match(seg):
                return False
        return True

    def _pins_read(self, client):
        """Pinned paths + doc _rev; ([], None) when not pinned yet (404)."""
        status, doc = client.get(self.notes_cfg.db_url + "/" + PINS_DOC_ID)
        if status == 200 and isinstance(doc, dict):
            paths = doc.get("paths")
            paths = paths if isinstance(paths, list) else []
            return [p for p in paths if isinstance(p, str)], doc.get("_rev")
        if status == 404:
            return [], None
        raise couchdb_client.CouchError(status, doc)

    def _pins_write(self, client, paths, rev):
        doc = {"_id": PINS_DOC_ID, "type": "pins", "paths": paths}
        if rev:
            doc["_rev"] = rev
        status, body = client.put(self.notes_cfg.db_url + "/" + PINS_DOC_ID, doc)
        if status not in (201, 202):
            raise couchdb_client.CouchError(status, body)
        return body

    def _handle_pins_get(self):
        try:
            client = couchdb_client.Client(self.notes_cfg)
            paths, _rev = self._pins_read(client)
        except Exception as exc:
            self._send_json(
                {"status": "error", "message": "CouchDB unavailable: %s" % exc},
                502,
            )
            return
        self._send_json({"pins": paths})

    def _handle_pins_post(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length) if length else b"{}")
        except json.JSONDecodeError as exc:
            self._send_json(
                {"status": "error", "message": "Invalid JSON: %s" % exc}, 400
            )
            return

        path_arg = payload.get("path") if isinstance(payload, dict) else None
        pinned = payload.get("pinned") if isinstance(payload, dict) else None
        if not self._valid_note_path(path_arg) or not isinstance(pinned, bool):
            self._send_json(
                {
                    "status": "error",
                    "message": 'body must be {"path": "<note path>",'
                               ' "pinned": true|false}',
                },
                400,
            )
            return

        try:
            client = couchdb_client.Client(self.notes_cfg)
            paths, rev = self._pins_read(client)
            if pinned and path_arg not in paths:
                paths.append(path_arg)
            elif not pinned and path_arg in paths:
                paths.remove(path_arg)
            self._pins_write(client, paths, rev)
        except Exception as exc:
            self._send_json(
                {"status": "error", "message": "CouchDB unavailable: %s" % exc},
                502,
            )
            return

        self._send_json({"status": "ok", "pins": paths})

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


def _couchdb_ready(ds):
    """Preflight one dataset: CouchDB + its database must be reachable."""
    client = couchdb_client.Client(ds.cfg)

    try:
        status, body = client.get(ds.cfg.url + "/")
    except Exception as exc:
        print(
            "[fatal] %s: CouchDB unreachable at %s: %s"
            % (ds.name, ds.cfg.url, exc),
            file=sys.stderr,
        )
        return False

    if status != 200:
        print(
            "[fatal] %s: CouchDB at %s returned HTTP %s"
            % (ds.name, ds.cfg.url, status),
            file=sys.stderr,
        )
        return False

    try:
        status, body = client.get(ds.cfg.db_url)
    except Exception as exc:
        print(
            "[fatal] %s: cannot check database '%s': %s"
            % (ds.name, ds.cfg.db, exc),
            file=sys.stderr,
        )
        return False

    if status == 404:
        print(
            "[fatal] %s: database '%s' not found on %s"
            " (create it: curl -u <user>:<pass> -X PUT %s/%s — see README)"
            % (ds.name, ds.cfg.db, ds.cfg.url, ds.cfg.url, ds.cfg.db),
            file=sys.stderr,
        )
        return False

    if status != 200:
        print(
            "[fatal] %s: database '%s' check returned HTTP %s"
            % (ds.name, ds.cfg.db, status),
            file=sys.stderr,
        )
        return False

    doc_count = body.get("doc_count") if isinstance(body, dict) else None
    print(
        "[ok] %s: database ready (doc_count=%s)" % (ds.name, doc_count)
    )
    return True


def main():
    parser = argparse.ArgumentParser(
        prog="serve.py",
        description="Epistecnica combined server (hub + epistemica + tecnica).",
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

    datasets = build_datasets()
    notes_cfg = envutil.dataset("NOTES_DB", "notes")

    for ds in datasets:
        if not ds.app_dir.exists():
            print(
                "ERROR: %s static dir not found: %s" % (ds.name, ds.app_dir),
                file=sys.stderr,
            )
            return 1

    notes_app = REPO / NOTES_MOUNT
    if not notes_app.is_dir():
        print("ERROR: notes static dir not found: %s" % notes_app, file=sys.stderr)
        return 1
    for prefix, mount in (
        ("course", COURSE_MOUNT),
        ("document", DOCUMENT_MOUNT),
        ("persona", PERSONA_MOUNT),
    ):
        app_dir = REPO / mount
        if not app_dir.is_dir():
            print("ERROR: %s static dir not found: %s" % (prefix, app_dir), file=sys.stderr)
            return 1
    glossarium_app = REPO / GLOSSARIUM_MOUNT
    if not glossarium_app.is_dir():
        print("ERROR: glossarium static dir not found: %s" % glossarium_app, file=sys.stderr)
        return 1
    hub_page = REPO / "src" / "app" / "index.html"
    if not hub_page.exists():
        print("ERROR: hub page not found: %s" % (hub_page,), file=sys.stderr)
        return 1

    for ds in datasets:
        if not _couchdb_ready(ds):
            print(
                "[fatal] Startup aborted: CouchDB backend is required for %s."
                % ds.name,
                file=sys.stderr,
            )
            return 1

    handler = partial(HubHandler, datasets=datasets, notes_cfg=notes_cfg)

    server = HTTPServer((args.host, args.port), handler)

    display_host = "localhost" if args.host in ("0.0.0.0", "::") else args.host

    print("══════════════════════════════════════════════")
    print("  Epistecnica Server (hub + CouchDB backends)")
    print("──────────────────────────────────────────────")
    print("  Hub:     http://%s:%d/" % (display_host, args.port))
    for ds in datasets:
        print(
            "  %-10s http://%s:%d%s/  (CouchDB: %s/%s)"
            % (ds.name + ":", display_host, args.port, ds.prefix, ds.cfg.url, ds.cfg.db)
        )
    print("  Health:  http://%s:%d%s" % (display_host, args.port, HUB_HEALTH_ENDPOINT))
    print("  Notes:   http://%s:%d%s/  (pins: CouchDB %s/%s)"
          % (display_host, args.port, NOTES_PREFIX, notes_cfg.url, notes_cfg.db))
    print("  Courses: http://%s:%d%s/" % (display_host, args.port, COURSE_PREFIX))
    print("  Docs:    http://%s:%d%s/" % (display_host, args.port, DOCUMENT_PREFIX))
    print("  Personas:http://%s:%d%s/" % (display_host, args.port, PERSONA_PREFIX))
    print("  Gloss.:  http://%s:%d%s/" % (display_host, args.port, GLOSSARIUM_PREFIX))
    print("══════════════════════════════════════════════")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    raise SystemExit(main())
