#!/usr/bin/env python3
"""
Tiny stdlib .env loader for the Epistecnica combined server.

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
