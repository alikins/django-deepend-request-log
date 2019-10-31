#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open

from setuptools import setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


setup(
    name='django-deepend-request-log',
    version='0.1.0',
    description='Django request logging middleware that logs so much stuff',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/alikins/django-deepend-request-log.git',
    author='Adrian Likins',
    author_email='alikins@gmail.com',
    license='MIT',
    packages=['deependrequestlog'],
    install_requires=[
        'django-log-request-id',
    ],
    zip_safe=False
)
