#!/usr/bin/env python

"""
Install piglatin package. To install locally use:
    'pip install -m ."
"""

from setuptools import setup

setup(
    name="piglatin",
    version="0.0.1",
    packages=[],
    entry_points={
        "console_scripts": ["piglatin = piglatin.__main__:run_program"]
    }
)