#!/usr/bin/python3
"""Function that returns the list of attribute and object."""


def lookup(obj):
    """Return a list of available attributes."""
    return (dir(obj))
