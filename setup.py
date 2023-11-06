#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="bitget-python",
    version="0.0.1",
    packages = find_packages(),
    install_requires=['requests', 'websockets']
)
