#!/usr/bin/env python3
from setuptools import setup, find_packages
NAME = "bitget"

setup(
    name="bitget",
    version="0.3.3",
    packages = find_packages(),
    install_requires=['requests', 'websockets']
)
