#! /usr/bin/env python3
"""Install MARS web services."""
# See: https://packaging.python.org/en/latest/distributing/

from setuptools import setup, find_packages 
from codecs import open  # To use a consistent encoding
from os import path
from glob import glob

here = path.abspath(path.dirname(__file__))
#!print('here={}'.format(here))

# Get the long description from the relevant file
#!with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
#!    long_description = f.read()
long_description="Provide webservices to access Archive related info."

with open(path.join(here,'marssite', 'water', 'VERSION')) as f:
    version = f.read().strip()
with open(path.join(here,'marssite', 'water', 'UPDATED')) as f:
    updated = f.read().strip()


setup(
    name='mars',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=version,

    description='Metadata Archive Retrival Services',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pothiers/mars',

    # Author details
    author='The Python Packaging Authority',
    author_email='pypa-dev@googlegroups.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Scientific/Engineering :: Astronomy',
 
       # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='webservices big-data astronomy archive',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=[
        'python-dateutil>=2.1',
        'pytz>=2013.9',
        'icalendar>=3.8.4',
        'django-annoying>=0.8.0'
    ],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #!package_data={
    #!    'tada_support': ['personalities/*', 'scripts/*', 'dev-scripts/*',],
    #!},
    package_data={'marssite': ['water/VERSION','water/UPDATED',
                               'static/*', 'static/*/*',
                               '*/static/*/*',
                               '*/templates/*/*',
    ]},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #!data_files=[('my_data', ['data/data_file'])],
    #!data_files=[('/etc/mars', glob('RELEASE-*.txt')),  ],


    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
        ],
    },
)
