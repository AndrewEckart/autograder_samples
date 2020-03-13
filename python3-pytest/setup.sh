#!/usr/bin/env bash
apt-get update
apt-get install -y python3 python3-pip python3-dev
pip3 install pytest
pip3 install pylint
pip3 install pytest-json
pip3 install subprocess32 gradescope-utils
