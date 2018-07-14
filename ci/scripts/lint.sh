#!/bin/sh
set -e

cd amiller_im_git

pylint --version
echo ""
ls -alh
echo ""
pylint amiller_im_git

