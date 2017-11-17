#!/bin/sh
echo $1


#while [ ! -r "$1" ]
#do
#    sleep 2s
#done

stat $1
# do processing here

currentstatus=`cat status`

python predict_on_image.py $1
if [ $? -eq 1 ]
then
    result="on"
else
    result="off"
fi

echo result: $result

if [ $result != $currentstatus ]
then
    echo $result > status
    case "$result" in
        "on") ./playmusic.sh
        ;;
        "off") ./pausemusic.sh
        ;;
    esac
fi


# fixme: issues deleting the file sometimes
rm *.jpg
