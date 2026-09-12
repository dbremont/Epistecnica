#!/bin/sh
set -eu

# Local deployment: build this repo and run the local image
# (dev/testing against a local CouchDB).
#
# For the production path (pull the GHCR image), use ./deploy-server.sh.

IMAGE="epistecnica:local"
CONTAINER="epistecnica"
PORT="${EPISTECNICA_PORT:-8000}"

cd "$(dirname "$0")"

# Mount the repo's .env into the container (CouchDB credentials etc.).
# bin/envutil.py reads it from /srv/.env. Real env vars still win (setdefault).
ENV_MOUNT=""
if [ -f .env ]; then
  ENV_MOUNT="-v ${PWD}/.env:/srv/.env:ro"
fi

docker build -t "$IMAGE" .
docker rm -f "$CONTAINER" 2>/dev/null || true
# shellcheck disable=SC2086
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  --network host \
  $ENV_MOUNT \
  "$IMAGE" \
  python bin/serve.py --port "$PORT"
