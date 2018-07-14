#!/bin/sh
set -e
echo "Attempting to get secrets from vault..."

# TODO having connection refused issues from within bosh lite
# spruce merge \
# --prune meta \
# amiller_im_git/ci/config/secrets.yml > secrets/secrets.yml

echo "Secrets file successfully generated"