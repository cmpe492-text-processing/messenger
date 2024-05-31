#!/bin/sh -e

DIR="$(dirname "$(realpath "$0")")"
"$DIR/.venv/bin/python" "$DIR/main.py"
