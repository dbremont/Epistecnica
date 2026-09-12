#!/bin/sh
set -eu

# Epistecnica deployment — two modes:
#
#   ./deploy.sh          # server mode (default): pull ghcr.io/dbremont/epistecnica:latest
#   ./deploy.sh server   #   (CI pushes this image on every push to main)
#   ./deploy.sh local    # local mode: docker build this repo and run the local image
#
# Both modes run the same container ("epistecnica", --network host) on
# EPISTECNICA_PORT (default 8000), mounting the repo's .env read-only.
# The container replaces the old "tecnica" (:8000) and "epistemica" (:8010)
# deployments — retire those when switching over.

IMAGE_REMOTE="ghcr.io/dbremont/epistecnica:latest"
IMAGE_LOCAL="epistecnica:local"
CONTAINER="epistecnica"
PORT="${EPISTECNICA_PORT:-8000}"

cd "$(dirname "$0")"

usage() {
  echo "usage: ./deploy.sh [server|local]"
  echo "  server (default)  pull $IMAGE_REMOTE and run it"
  echo "  local             docker build the repo and run $IMAGE_LOCAL"
}

MODE="${1:-server}"

# Mount the repo's .env into the container (CouchDB credentials etc.).
# bin/envutil.py reads it from /srv/.env. Real env vars still win (setdefault).
ENV_MOUNT=""
if [ -f .env ]; then
  ENV_MOUNT="-v ${PWD}/.env:/srv/.env:ro"
fi

case "$MODE" in
  server)
    IMAGE="$IMAGE_REMOTE"
    docker pull "$IMAGE"
    ;;
  local)
    IMAGE="$IMAGE_LOCAL"
    docker build -t "$IMAGE" .
    ;;
  *)
    usage
    exit 1
    ;;
esac

docker rm -f "$CONTAINER" 2>/dev/null || true
# shellcheck disable=SC2086
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  --network host \
  $ENV_MOUNT \
  "$IMAGE" \
  python bin/serve.py --port "$PORT"
