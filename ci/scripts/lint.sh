#!/bin/sh
set -e

cd amiller_im_git

pylint3 --version
echo ""
ls -alh
echo ""
# TODO Do This beetter with env
pylint3 app

