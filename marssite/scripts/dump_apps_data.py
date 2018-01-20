#! /usr/bin/env python3
"""Save DB for each app.
"""
# Docstrings intended for document generation via pydoc

import sys
import argparse
import logging


import pathlib
from django.apps import apps
from django.core import management

my_apps = [
    'audit',
    'natica',
    'provisional',
    'schedule',
    #@@@'siap',
    'tada',
    'water',
    ]


#! for my_app in my_apps:
#!     for c in apps.get_app_config(my_app).get_models():
#!         print('app.model='.format(my_app, c.__name__))


#! export DJANGO_SETTINGS_MODULE=marssite.marssite.settings

def dump_apps_data(destdir=None, apps=None):
    if apps == None:
        apps = my_apps
    for myapp in apps:
        outpath = pathlib.PurePath(destdir, myapp+'.yaml')
        print('dump django models to: {}, myapp={}'.format(str(outpath), myapp))
        management.call_command('dumpdata',
                                '--format=yaml',
                                '--indent=4',
                                '--output={}'.format(str(outpath)),
                                myapp)


##############################################################################

def main():
    "Parse command line arguments and do the work."
    parser = argparse.ArgumentParser(
        description='Save DB data from MARS apps',
        epilog='EXAMPLE: %(prog)s"'
        )
    dflt_destdir = pathlib.Path.cwd()
    dflt_apps = my_apps
    parser.add_argument('--version', action='version', version='1.0.1')
    parser.add_argument('--destdir',
                        default=dflt_destdir,
                        help=('Destination directory for generated YAML files. '
                              '[default={}]'.format(dflt_destdir)))
    parser.add_argument('--apps',
                        default=dflt_apps,
                        help=('List of apps to dump data from. '
                              '[default={}]'.format(dflt_apps)))

    parser.add_argument('--loglevel',
                        help='Kind of diagnostic output',
                        choices=['CRTICAL', 'ERROR', 'WARNING',
                                 'INFO', 'DEBUG'],
                        default='WARNING')
    args = parser.parse_args()

    log_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(log_level, int):
        parser.error('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=log_level,
                        format='%(levelname)s %(message)s',
                        datefmt='%m-%d %H:%M')
    logging.debug('Debug output is enabled in %s !!!', sys.argv[0])

    dump_apps_data(destdir=args.destdir, apps=args.apps)

if __name__ == '__main__':
    main()

