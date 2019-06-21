#!/usr/bin/env python
# -*- coding: utf-8 -*

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='nameko-extras',
    version='0.2.0',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    description='Nameko run with autoloading, logging file CLI option',
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    maintainer='Chatbot Developers',
    maintainer_email='chatbot-developers@babylonhealth.com',
    license='Apache License 2.0',
    long_description=(
        'https://github.com/Babylonpartners/nameko-extras'
    ),
    entry_points={
        'console_scripts': [
            'nameko_extras=nameko_extras.cli.main:main',
        ],
    },
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
