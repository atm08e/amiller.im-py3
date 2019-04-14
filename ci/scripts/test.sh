#!/bin/sh
set -e
datetime
cd /opt/amiller-im-py3
echo "Trying to run unit tests!"
python --version
pip freeze
python -m unittest tests.test_amiller_im


