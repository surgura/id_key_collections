#!/bin/sh

cd "$(dirname "$0")"

isort --profile black ../../id_key_collections ../../tests
