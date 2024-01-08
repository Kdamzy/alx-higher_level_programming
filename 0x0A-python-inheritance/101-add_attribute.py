#!/usr/bin/python3
"""A function attributes."""


def add_attribute(obj, att, value):
    """Add a new attribute to the object(obj).
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
