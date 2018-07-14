#!/bin/sh
set -e

pylint --version
echo ""
ls -alh
echo ""
pylint amiller_im_git

