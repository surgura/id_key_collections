#!/bin/sh

cd "$(dirname "$0")"
dirs="../../id_key_collections"
find $dirs -type f -name '__init__.py' -print0 | xargs -0 sort-all
