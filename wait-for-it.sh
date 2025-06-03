#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

set -e

HOST="$1"
PORT="$2"
shift 2
CMD="$@"

until nc -z "$HOST" "$PORT"; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

echo "$HOST:$PORT is available. Running command: $CMD"
exec $CMD
