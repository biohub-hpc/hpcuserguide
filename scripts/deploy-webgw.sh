#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}

# Make the site.
foliant make site || die "Failed running 'foliant make site'"

# Push site to webgw.czbiohub.org
rsync -rv --progress --delete hpc-user-guide.mkdocs/ root@webgw.czbiohub.org:/var/www/hpc.czbiohub.org/html/

