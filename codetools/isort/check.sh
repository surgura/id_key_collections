#!/bin/sh

cd "$(dirname "$0")"

isort --check-only --diff --profile black ../../id_key_collections
