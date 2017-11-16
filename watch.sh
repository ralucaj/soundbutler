#!/bin/sh
fswatch -0 -I -e ".*" -i "\\.jpg" . | xargs -0 -n1 ./process.sh
