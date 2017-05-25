import os
import setuptools
import sys

from setuptools import setup

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')	 
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lambda_packages',
    version='0.15.1',
    packages=['lambda_packages'],
    include_package_data=True,
    license='MIT License',
    description='AWS Lambda Packages',
    long_description=README,
    url='https://github.com/Miserlou/lambda-packages',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
