#!/usr/bin/env python3

from setuptools import setup, find_packages
import re

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    with open('captchasio/__init__.py', 'r') as f:
        return re.search(r'__version__ = ["\'](.*?)["\']', f.read()).group(1)


setup(name='captchas.io-python',
      version=get_version(),
      description='Python library or module integrated with the CAPTCHAs.IO API web service for automating CAPTCHA solving.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/captchasio/captchas.io-python',
      install_requires=['requests'],
      author='CAPTCHAs.IO',
      author_email='admin@captchas.io',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.7',
      test_suite='tests')
