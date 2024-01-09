#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Function that return the dictionary represntation of json."""
    return obj.__dict__
