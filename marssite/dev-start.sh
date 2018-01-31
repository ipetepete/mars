#!/bin/bash
dir=`dirname $0`
SCRIPT=$(readlink -f $0)      #Absolute path to this script
SCRIPTPATH=$(dirname $SCRIPT) #Absolute path this script is in


#LOG=$HOME/mars.log
LOG=/var/log/mars/server.log

#pkill -f gunicorn
pkill -f "manage.py runserver"

echo "Running NATICA from: $SCRIPTPATH"
pushd $SCRIPTPATH
# NB: "unbuffer" is a small script that comes with the "excpect" package
nohup unbuffer python3 -u manage.py  runserver 0.0.0.0:8000 >  /var/log/mars/server.log &
#echo "tail -F $LOG"
#tail -F $LOG


# Stop this server with:
#   sudo pkill -f "manage.py runserver"

