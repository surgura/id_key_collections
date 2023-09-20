#!/bin/sh

cd "$(dirname "$0")"

black --diff --check ../../id_key_collections ../../tests
