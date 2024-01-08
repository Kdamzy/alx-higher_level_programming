#!/usr/bin/python3
"""A class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to be checked.
        a_class: The class to match the type of object.
    Returns:
        boolean value of a_class - True if the object is an instance.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
