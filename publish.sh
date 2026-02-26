#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -f "$SCRIPT_DIR/.env" ]; then
  echo "Error: .env file not found. Copy .env.example and fill in your token."
  exit 1
fi

source "$SCRIPT_DIR/.env"

if [ -z "$PYPI_TOKEN" ]; then
  echo "Error: PYPI_TOKEN is not set in .env"
  exit 1
fi

echo "Publishing to PyPI. Are you sure? (y/N)"
read -r confirm
if [ "$confirm" != "y" ]; then
  echo "Aborted."
  exit 0
fi

uv build

uv publish --token "$PYPI_TOKEN"
