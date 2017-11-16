#!/bin/sh
. config
echo $PLAYER Pausing
osascript -e 'tell app "'$PLAYER'" to pause'
