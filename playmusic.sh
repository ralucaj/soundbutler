#!/bin/sh
. config
echo $PLAYER Playing
osascript -e 'tell app "'$PLAYER'" to play'
