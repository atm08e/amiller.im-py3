#!/bin/bash
pwd
echo $PATH
ls -alh
ls -alh /opt/amiller-im-py3

cd /opt/amiller-im-py3
echo "Trying to lint!"
pylint --version
pylint app --errors-only
echo "Done linting!"

