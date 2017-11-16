#!/bin/sh
echo $1


#while [ ! -r "$1" ]
#do
#    sleep 2s
#done

stat $1
# do processing here

currentstatus=`cat status`

result=`./analyze.sh $1`

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
