#!/usr/bin/env python3

from setuptools import setup, find_packages
from PfsenseFauxapi.__version__ import __version__

setup(
    name='pfsense-fauxapi',
    version=__version__,
    description='Python client for the pfSense-FauxAPI on a pfSense host',

    classifiers=[
        'Topic :: System :: Networking :: Firewalls',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='pfsense pfsense-fauxapi devops',

    author='Nicholas de Jong',
    author_email='contact@nicholasdejong.com',
    url='https://github.com/ndejong/pfsense_fauxapi',
    license='Apache',

    packages=find_packages(),
    scripts=['bin/fauxapi'],
    install_requires=['requests'],

)
