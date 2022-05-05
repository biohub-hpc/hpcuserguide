#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}

# Make the site.
foliant make site || die "Failed running 'foliant make site'"

# Push site to hpc.czbiohub.org
rsync -rv --progress --delete hpc-user-guide.mkdocs/ root@hpc.czbiohub.org:/var/www/html/

