#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA
import os.path

try:
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        requirements = [i for i in f if not i.startswith('#')]
except IOError:
    requirements = []

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='repeat',
    version='0.1.0',
    py_modules=['repeat'],
    author='Park, Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park, Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='',
    description='Repeat command N times every M seconds',
    install_requires=requirements,
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'repeat = repeat:main',
        ],
    },
)
