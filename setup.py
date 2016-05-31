# -*- coding: utf8 -*-
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='python-brasileirao',
    version='0.0.1',
    description='',
    long_description=open(README).read(),
    author='Anderson Lima',
    author_email='anderson.sl93@hotmail.com',
    license="MIT",
    py_modules=['brasileirao'],
    platforms='any',
    url='https://github.com/TheKiller666/python-brasileirao',
    packages=['python-brasileirao'],
    install_requires=[
        'requests'
    ]
)
