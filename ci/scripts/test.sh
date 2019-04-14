#!/bin/sh
set -e
pwd
datetime
cd /opt/amiller-im-py3
echo "Trying to run unit tests!"
python --version
pip freeze
python -m unittest tests.test_amiller_im


