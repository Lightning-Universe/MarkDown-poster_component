#!/usr/bin/env python
import os

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


setup(
    name="markdown-poster",
    version="0.1.0",
    description="Render Markdowns in your Lightning app",
    author="Grid.ai",
    author_email="",
    url="https://github.com/PyTorchLightning/markdown-poster",
    install_requires=_load_requirements(),
    packages=find_packages(),
)
