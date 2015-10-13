#! /usr/bin/env python3
'''Get schedules in XML format for a bunch of dates and telescopes.'''

import sys
import argparse
import logging
import subprocess
from datetime import date, datetime, timedelta as td

def getxml(outxml, begindate, enddate):
    '''begin/enddate :: DATE object'''

    telescope_list = 'ct09m,ct13m,ct15m,ct1m,ct4m,gem_n,gem_s,het,keckI,keckII,kp09m,kp13m,kp21m,kp4m,kpcf,magI,magII,mmt,soar,wiyn'.split(',')

    # getschedulexml.pl -tel=wiyn -date=2015-09-01 > wiyn.2015-09-01.schedule.xml
    cmdstr = '/home/pothiers/sandbox/mars/marssite/schedule/getschedulexml.pl -tel={telescope} -date={date}'
    #cmd = cmdstr.split()

    delta = enddate - begindate
    with open(outxml, 'w') as f:
        print('<all>', file=f, flush=True)
        for tele in telescope_list:
            for i in range(delta.days + 1):
                obsdate = begindate + td(days=i)
                out = subprocess.check_call(cmdstr.format(telescope=tele, date=obsdate),
                                            shell=True,
                                            stdout=f)
        print('</all>', file=f)                



##############################################################################

def main():
    "Parse command line arguments and do the work."
    print('EXECUTING: %s\n\n' % (' '.join(sys.argv)))
    parser = argparse.ArgumentParser(
        description='My shiny new python program',
        epilog='EXAMPLE: %(prog)s a b"'
        )
    parser.add_argument('--version', action='version', version='1.0.1')
    parser.add_argument('outxml', type=argparse.FileType('w'),
                        help='Output XML file')
    
    parser.add_argument('--begindate',
                        help='First date (YYYY-MM-DD) for returned schedule [default=today]')
    parser.add_argument('--enddate', 
                        help='Last date for returned schedule. [default=begindate]')


    parser.add_argument('--loglevel',
                        help='Kind of diagnostic output',
                        choices=['CRTICAL', 'ERROR', 'WARNING',
                                 'INFO', 'DEBUG'],
                        default='WARNING')
    args = parser.parse_args()
    args.outxml.close()
    args.outxml = args.outxml.name


    log_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(log_level, int):
        parser.error('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=log_level,
                        format='%(levelname)s %(message)s',
                        datefmt='%m-%d %H:%M')
    logging.debug('Debug output is enabled in %s !!!', sys.argv[0])

    if args.begindate == None:
        bdate = date.today()
    else:
        bdate = datetime.strptime(args.begindate,'%Y-%m-%d').date()

    if args.enddate == None:
        edate = bdate
    else:
        edate = datetime.strptime(args.enddate,'%Y-%m-%d').date()
        
    getxml(args.outxml, bdate, edate)

if __name__ == '__main__':
    main()

        