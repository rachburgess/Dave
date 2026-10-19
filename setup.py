#!/usr/bin/env python3
"""Setup script for Dave Python package."""

import sys
from setuptools import setup, find_packages

# PEP 563: Postponed evaluation of annotations (Python 3.7+)
if sys.version_info >= (3, 8):
    from typing import Dict, List
elif sys.version_info >= (3, 10):
    from typing import TYPE_CHECKING
else:
    from typing_extensions import TypeAlias, TypedDict

# Add __init__ directory for the package
import os
dave_dir = os.path.join(os.path.dirname(__file__), 'Dave')
if not os.path.exists(dave_dir):
    os.makedirs(dave_dir)

with open(os.path.join('Dave', '__init__.py'), 'w') as f:
    if sys.version_info >= (3, 8):
        f.write('from __future__ import annotations\n\n')
    else:
        f.write('from __future__ import annotations\n')
    
    f.write('''"""
Dave - Cross-platform Python Application

This package provides platform-specific functionality for Dave.

Supports Windows, Linux, macOS, and Android platforms.
"""

VERSION = "1.0.0"


def get_platform() -> str:
    """Get the current platform."""
    from sys import platform as _platform
    
    mapping = {
        'win32': 'windows',
        'darwin': 'macos',
        'linux': 'linux',
        'android': 'android'
    }
    
    return mapping.get(_platform, f"unknown ({_platform})")


__all__ = ['get_platform', 'VERSION']
''')

setup(
    name='dave',
    version='1.0.0',
    author='rachburgess',
    author_email='rachburgess@gmail.com',
    description='Cross-platform Python application for various operating systems',
    long_description=open('README.md').read() if os.path.exists('README.md') else None,
    long_description_content_type='text/markdown',
    url='https://github.com/rachburgess/Dave',
    project_urls={
        'Bug Tracker': 'https://github.com/rachburgess/Dave/issues'
    },
    license='MIT',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    packages=find_packages(where='Dave'),
    include_package_data=True,
    package_dir={'': 'Dave'},
    install_requires=[
        'requests>=2.20.0',
        'json>=2.0.0; python_version > "3.10"',
    ],
)
