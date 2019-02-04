# -*- coding: utf-8 -*-

# @Author: hyan15
# @Email: qwang16@olivetuniversity.edu

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(path.join(here, 'amazon_page_parser', 'VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='amazon-page-parser',
    version=version,
    description='A library for parsing amazon pages.',
    long_description=long_description,
    url='',
    author='hyan15',
    author_email='qwang16@olivetuniversity.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    keywords='amazon scrape scraper',
    packages=['amazon_page_parser'],
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'parsel'
    ]
)
