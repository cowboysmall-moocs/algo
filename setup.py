#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='algorithms1',
    version='0.1.0',
    description='Algorithms Design and Analysis Part 1 contains all programming exercises for the Coursera course',
    author='Jerry Kiely',
    author_email='jerry@cowboysmall.com',
    url='https://github.com/cowboysmall/algorithms1',
    packages=['algorithms1',],
    package_dir={'algorithms1': 'algorithms1'},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords='algorithms1',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)