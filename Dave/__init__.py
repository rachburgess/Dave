"""
Dave - Cross-platform Python Application

This package provides platform-specific functionality for Dave.

Supports Windows, Linux, macOS, and Android platforms.
"""

import sys

VERSION = "1.0.1"


def get_platform() -> str:
    """Get the current platform."""
    mapping = {
        'win32': 'windows',
        'darwin': 'macos',
        'linux': 'linux',
        'android': 'android'
    }
    
    return mapping.get(sys.platform, f"unknown ({sys.platform})")


__all__ = ['get_platform', 'VERSION']
