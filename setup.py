#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


version = "0.1"

setup(
    name="djutil",
    version=version,
    description="Common Django utilities",
    license="MIT",

    author="Filip Wasilewski",
    author_email="en@ig.ma",

    url="https://github.com/nigma/djutil",
    download_url="https://github.com/nigma/djutil/zipball/master",

    long_description=open("README.rst").read(),

    packages=["djutil"],
    package_dir={"djutil": "src"},
    include_package_data=True,
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ),
    tests_require=["django>=1.5"]
)
