#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}


# Sites we know how to deploy.
declare -A SITES
SITES["hpc-user-guide"]="hpc.czbiohub.org:/var/www/html/hpc-user-guide"
SITES["hpc-admin-guide"]="NONE"

# See what site we are working in.
SITE=$(basename $PWD)
[[ -n ${SITES[${SITE}]} ]] || die "Unknonwn site ${SITE}"


while foliant make mkdocs; do
  pushd ${SITE}.mkdocs.src
    mkdocs serve || exit 1
  popd
done
