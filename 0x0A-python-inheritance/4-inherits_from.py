#!/usr/bin/python3
"""An inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to be compared.
    Returns:
        Boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
