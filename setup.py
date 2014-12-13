#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import visualizer
version = visualizer.__version__

setup(
    name='mfp',
    version=version,
    author='',
    author_email='simcha.levental@gmail.com',
    packages=[
        'visualizer',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['visualizer/manage.py'],
)
