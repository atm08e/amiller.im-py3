#!/bin/sh
set -e

echo "Building venv"
cd amiller_im_git
python3 -m venv venv
venv/bin/pip install -r requirements.txt
cd -rfv venv ../venv
