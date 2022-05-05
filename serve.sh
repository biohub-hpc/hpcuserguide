#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}


while foliant make mkdocs; do
  pushd hpc-user-guide.mkdocs.src
    mkdocs serve || exit 1
  popd
done
