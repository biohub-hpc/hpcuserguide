#!/usr/bin/env bash

function die () {
  echo "ERROR: $*"
  exit 1
}

# Make the site.
foliant make site || die "Failed running 'foliant make site'"

# Push site to webgw.czbiohub.org via local NFS mount
rsync -rv --progress --delete hpc-user-guide.mkdocs/ /hpc/websites/hpc.czbiohub.org/html/

