#!/bin/sh
set -e

cd amiller_im_git

pylint --version
echo ""
ls -alh
echo ""
pip install -r requirements.txt

# TODO Do This beetter with env
pylint app --errors-only

