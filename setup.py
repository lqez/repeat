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
    'Topic :: Terminals',
    'Topic :: Utilities',
    'Environment :: Console',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='repeat',
    version='0.1.1',
    py_modules=['repeat'],
    author='Park, Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park, Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/repeat',
    description='Repeat command N times every S seconds.',
    install_requires=requirements,
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'repeat = repeat:main',
        ],
    },
)
