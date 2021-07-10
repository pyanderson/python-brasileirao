import os

from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='python-brasileirao',
    version='1.0.0',
    description='',
    long_description=open(README).read(),
    author='Anderson Lima',
    author_email='anderson.sl93@hotmail.com',
    license="MIT",
    py_modules=['brasileirao'],
    platforms='any',
    url='https://github.com/pyanderson/python-brasileirao',
    install_requires=[
        'requests',
        'inflection'
    ]
)
