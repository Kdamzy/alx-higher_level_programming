#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
    Args:
        obj: The object to check.
        a_class: The class to compare the type of obj to.
    Returns:
        Boolean value of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
