# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="assignmenttest",
    version="0.0.3",
    license="MIT",
    url="https://github.com/DigiKlausur/assignmenttest",
    description="Create test cases for Python assignments",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tim Metzler",
    author_email="tim.metzler@h-brs.de",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=["rapidfuzz", "e2xgradingtools"],
    include_package_data=True,
    zip_safe=False,
)
