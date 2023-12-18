#!/usr/bin/python3

import os

from setuptools import setup, find_packages

current_folder = os.path.abspath(os.path.dirname(__file__))
version_file_path = current_folder + "/ai21/version.py"

version_file = {}
with open(version_file_path, "rt") as f:
    exec(f.read(), version_file)
version = version_file["__version__"]

setup(
    name="ai21",
    version=version,
    license="MIT",
    author="ai21 labs",
    author_email="support@ai21.com",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests",
    ],
    # extras_require={"AWS": ["boto3>=1.28.82"]},
)
