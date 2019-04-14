#!/bin/bash
pwd
date
cd /opt/amiller-im-py3
echo "Trying to run unit tests!"
python3 --version
pip3 freeze
pytho3 -m unittest tests.test_amiller_im


