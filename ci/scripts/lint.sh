#!/bin/sh
set -e
echo ""
ls -alh
echo ""

cd /opt/amiller-im-py3
echo "Trying to link!"
pylint --version
pylint app --errors-only

