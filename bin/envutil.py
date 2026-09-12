#!/usr/bin/env python3
"""
Tiny stdlib .env loader for the Epistecnica combined server.

Same behavior as the per-project bin/envutil.py scripts, plus per-dataset
database resolution: the combined repo uses ONE CouchDB instance with TWO
databases (epistemica, tecnica), selected via EPISTEMICA_DB / TECNICA_DB.

Reads <repo>/.env once, populates os.environ for keys that are not already
set (real environment variables win).
"""

import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / ".env"

_LOADED = False


def _load():
    global _LOADED
    if _LOADED:
        return
    _LOADED = True
    if not ENV_FILE.exists():
        return
    with open(ENV_FILE, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            os.environ.setdefault(key, val)


def _get(key, default=None):
    _load()
    return os.environ.get(key, default)


class CouchConfig:
    """Resolved CouchDB connection settings."""

    def __init__(self, url=None, db=None, user=None, password=None):
        self.url = (url or (_get("COUCHDB_URL") or "http://127.0.0.1:5984")).rstrip("/")
        self.db = db or _get("COUCHDB_DB") or "epistemica"
        self.user = user if user is not None else _get("COUCHDB_USER")
        self.password = password if password is not None else _get("COUCHDB_PASSWORD")

    @property
    def base(self):
        return self.url

    @property
    def db_url(self):
        return "%s/%s" % (self.url, self.db)

    def __repr__(self):
        return "CouchConfig(url=%r, db=%r, user=%r)" % (
            self.url,
            self.db,
            self.user,
        )


def couch():
    """Default config (single-DB fallback; standalone-style scripts)."""
    return CouchConfig()


def dataset(db_env_key, default_db):
    """Config for one dataset: COUCHDB_* plus a dataset-specific DB name."""
    return CouchConfig(db=_get(db_env_key) or default_db)
