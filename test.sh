#!/bin/bash
# EXAMPLE:
#   ~/sandbox/mars/smoke-test.sh

SCRIPT=$(readlink -e $0)     #Absolute path to this script
SCRIPTDIR=$(dirname $SCRIPT) #Absolute path this script is in

source /opt/mars/venv/bin/activate

cd $SCRIPTDIR/marssite

# sometimes errors with 'NoneType' object is not iterable
# Stack track doesn't point to mars at all.
#!./manage.py test 


#
# Using --keepdb over "--parallel 4" is about 3x faster after first time.
#
# There are cons to using keepdb and maybe higher parallel would be
# reasonable, but test speed is very important to DEV so trumps other aspects.
# Running under Travis CI will always have to create the new DBs since
# it gets a new VENV every time.
#

#!./manage.py test --parallel 4 schedule.tests_production schedule.tests_operations tada.tests provisional.tests audit.tests_production audit.tests_operations

   
#@@@@ ./manage.py test --settings=marssite.test_settings dal.tests
#./manage.py test --keepdb schedule.tests_production schedule.tests_operations tada.tests provisional.tests audit.tests_production audit.tests_operations
./manage.py test --keepdb schedule.tests_production schedule.tests_operations natica.tests  audit.tests_production audit.tests_operations dal.tests

#./manage.py test schedule.tests_production
#./manage.py test schedule.tests_operations
#./manage.py test tada.tests
#
#./manage.py test provisional.tests
#./manage.py test audit.tests_production
#./manage.py test audit.tests_operations

#! ./manage.py test water.tests
#! ./manage.py test siap.tests

#! ./manage.py test tada.tests.TadaTest.test_table_prefix

