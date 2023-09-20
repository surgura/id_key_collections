#!/bin/sh

cd "$(dirname "$0")"

darglint -s sphinx ../../id_key_collections ../../tests
