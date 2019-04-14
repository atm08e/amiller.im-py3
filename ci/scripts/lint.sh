#!/bin/sh
set -e

cd amiller_im_git

pylint --version
echo ""
ls -alh
echo ""
# TODO Do This beetter with env

# we really should build 1 docker image
pip install -r requirements

pylint app --errors-only

