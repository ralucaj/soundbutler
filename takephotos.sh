#/bin/sh
. config

unit=s
while [ 1 ]
do
  ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "0" -vframes 1   -q:v 1 -y  photo.jpg
  ./process.sh photo.jpg
  sleep $INTERVAL$unit
done

