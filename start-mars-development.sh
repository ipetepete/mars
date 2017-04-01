#!/bin/bash
dir=`dirname $0`
SCRIPT=$(readlink -f $0)      #Absolute path to this script
SCRIPTPATH=$(dirname $SCRIPT) #Absolute path this script is in

source /opt/mars/venv/bin/activate
$SCRIPTPATH/marssite/dev-start.sh
