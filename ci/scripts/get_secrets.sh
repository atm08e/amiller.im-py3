#!/bin/sh

echo "Attempting to get secrets from vault..."

spruce merge \
--prune meta \
amiller_im_git/ci/config/secrets.yml > secrets/secrets.yml

echo "Secrets file successfully generated"