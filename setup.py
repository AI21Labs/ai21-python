#!/usr/bin/python3

import os

from setuptools import setup, find_packages
from ai21.version import VERSION


with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()


setup(
    name="ai21",
    version=VERSION,
    license="MIT",
    author="AI21 Labs",
    author_email="support@ai21.com",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=["tests", "tests.*"]),
    keywords=["python", "sdk", "ai", "ai21", "jurassic", "ai21-python", "llm"],
    install_requires=[
        "requests",
    ],
)
