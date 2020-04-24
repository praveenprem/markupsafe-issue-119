#!/usr/bin/env python
import os

from setuptools import find_packages
from setuptools import setup

base_dir = os.path.dirname(__file__)

setup(
        name='test',
        version='0.0.1-preview',
        packages=find_packages(),
        install_requires=[
            'boto3==1.9.113',
            'dpath==1.4.2',
            'GitPython==2.1.15',
            'Jinja2==2.10',
            'requests==2.20.1',
            'sshtunnel==0.1.4',
            'semver==2.8.1',
            'python-consul==1.1.0',
            'jsonpath_rw==1.4.0',
            'appdirs==1.4.3'
            ],
        tests_require=[
            'requests==2.20.1',
            'mock'
        ],

)
