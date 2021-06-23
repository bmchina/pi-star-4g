#!/bin/bash

logfile="/var/log/usb4g.log"
actiontime=$(date +"%Y/%m/%d %H:%M:%S")
isrunning=$(ps aux | grep start4g.py | wc -l)
isrunning=$[isrunning-1]

if [ $isrunning -gt 0 ]
then
    sudo echo "Skip: -- "$actiontime >> $logfile 
    exit
else
    sudo echo "Run: -- "$actiontime >> $logfile
    sudo python /usr/local/bin/start4g.py
    exit
fi
