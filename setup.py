#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pybitcointools',
      version='1.1.42',
      description='Python Bitcoin Tools',
      author='Vitalik Buterin',
      author_email='vbuterin@gmail.com',
      url='http://github.com/vbuterin/pybitcointools',
      packages=['pybitcointools'],
      scripts=['pybtctool'],
      include_package_data=True,
      data_files=[("", ["LICENSE"]), ("pybitcointools", ["pybitcointools/english.txt"])],
      )
