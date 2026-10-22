# Epistecnica — project operations.
#
#   make deploy-local    build the local image and run the container (dev/testing)
#   make deploy-server   pull the GHCR image CI publishes and run it (production)
#
# Deploys require Docker and CouchDB running on 127.0.0.1:5984.

CONTAINER   := epistecnica
LOCAL_IMAGE := epistecnica:local
GHCR_IMAGE  := ghcr.io/dbremont/epistecnica:latest

# Port for the dev server (`make run`) — kept distinct from the deployed
# container's port so it never collides with it.
DEV_PORT ?= 8010

# Deploy port. Repo-local defaults (.env is git-ignored); loaded at parse
# time, so an EPISTECNICA_PORT=... line in .env applies. Explicit
# `make EPISTECNICA_PORT=...` overrides still win.
EPISTECNICA_PORT ?= 8000

# DB coordinates used by `make bootstrap` (same defaults as bin/envutil.py;
# .env values override). AUTH feeds the bootstrap curls — empty when
# COUCHDB_USER is unset (admin-party CouchDB). The ontology graphs moved to
# Naturgnosis; the only local DB is the notes-catalog pins store.
COUCHDB_URL   ?= http://127.0.0.1:5984
NOTES_DB      ?= notes
AUTH          = $(if $(COUCHDB_USER),-u "$(COUCHDB_USER):$(COUCHDB_PASSWORD)",)

-include .env
export

ifneq (,$(wildcard .env))
ENV_MOUNT := -v $(CURDIR)/.env:/srv/.env:ro
endif

.PHONY: help run check bootstrap notes-index course-index document-index rees-check search-index graph-index index changelog-link build deploy-local deploy-server logs stop

help: ## list targets
	@grep -E '^[a-zA-Z_-]+:.*## ' Makefile | awk 'BEGIN {FS = ":.*## "}; {printf "  %-15s %s\n", $$1, $$2}'

run: ## local dev server, no docker (port DEV_PORT, default 8010)
	python3 bin/serve.py --port $(DEV_PORT)

check: ## py_compile all servers + index builders + validate the REES tree
	python3 -m py_compile bin/*.py src/note/bin/*.py src/course/bin/*.py src/document/bin/*.py
	python3 src/note/bin/rees_check.py

notes-index: ## rebuild the notes search index (after any corpus change)
	python3 src/note/bin/index.py

course-index: ## rebuild the courses search index (after any corpus change)
	python3 src/course/bin/index.py

document-index: ## rebuild the documents search index (after any corpus change)
	python3 src/document/bin/index.py

rees-check: ## validate the REES tree store (src/note/app/data/epistemica/rees.json)
	python3 src/note/bin/rees_check.py

search-index: ## build the universal search snapshot (before build/deploy)
	python3 bin/build_search_index.py

graph-index: ## rebuild the universal view graph + layout (after any corpus change)
	python3 bin/build_universal_index.py
	python3 bin/layout.py --group-by source

index: notes-index course-index document-index search-index ## rebuild all search indexes (corpora first, universal snapshot last)

changelog-link: ## stamp commit links on corpus changelog logs introduced by HEAD
	python3 bin/link_changelog_commits.py

# One-time CouchDB setup. The create-then-verify idiom keeps the rule
# re-runnable (PUT on an existing DB would fail with 412). Credentials come
# from .env via AUTH when set.
bootstrap: ## one-time CouchDB setup: create the notes pins DB
	curl -fsS $(AUTH) -X PUT $(COUCHDB_URL)/$(NOTES_DB) || curl -fsS $(AUTH) -o /dev/null $(COUCHDB_URL)/$(NOTES_DB)
	curl -fsS $(AUTH) -X PUT $(COUCHDB_URL)/$(NOTES_DB)/_security -H 'Content-Type: application/json' -d '{}'

build: ## docker build the local image (epistecnica:local)
	docker build -t $(LOCAL_IMAGE) .

deploy-local: build ## build the local image and recreate container epistecnica
	$(call run_container,$(LOCAL_IMAGE))

deploy-server: ## pull the GHCR image and recreate container epistecnica
	docker pull $(GHCR_IMAGE)
	$(call run_container,$(GHCR_IMAGE))

logs: ## follow container epistecnica logs
	docker logs -f $(CONTAINER)

stop: ## stop and remove container epistecnica
	docker rm -f $(CONTAINER) 2>/dev/null || true

# Shared by both deploy targets: same semantics as the old deploy-*.sh — host
# network, restart policy, .env mounted read-only at /srv/.env (bin/envutil.py
# reads it there; real env vars win), and the port passed explicitly to
# bin/serve.py.
define run_container
	docker rm -f $(CONTAINER) 2>/dev/null || true
	docker run -d --name $(CONTAINER) --restart unless-stopped \
		--network host \
		$(ENV_MOUNT) \
		$(1) \
		python bin/serve.py --port "$(EPISTECNICA_PORT)"
endef
