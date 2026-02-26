#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -f "$SCRIPT_DIR/.env" ]; then
  echo "Error: .env file not found. Copy .env.example and fill in your token."
  exit 1
fi

source "$SCRIPT_DIR/.env"

if [ -z "$TESTPYPI_TOKEN" ]; then
  echo "Error: TESTPYPI_TOKEN is not set in .env"
  exit 1
fi

uv build

uv publish \
  --publish-url https://test.pypi.org/legacy/ \
  --token "$TESTPYPI_TOKEN"
