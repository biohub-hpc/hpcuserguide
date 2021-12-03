#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}

# Sites we know how to deploy.
declare -A SITES
SITES["hpc-user-guide"]="hpc.czbiohub.org:/var/www/html/hpc-user-guide"
SITES["hpc-admin-guide"]="hpc.czbiohub.org:/var/www/html/hpc-admin-guide"

# See what site we are working in.
SITE=$(basename $PWD)
[[ -n ${SITES[${SITE}]} ]] || die "Unknonwn site ${SITE}"

# Make the site.
foliant make site || die "Failed running 'foliant make site'"

# Push site to hpc.czbiohub.org
rsync -rv --progress ${SITE}.mkdocs/ ${SITES[${SITE}]}

