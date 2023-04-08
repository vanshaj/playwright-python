#!/bin/bash
python3 -m pytest tests --alluredir=/tmp/report --browser=chromium --slowmo 1000 --config-file config.json