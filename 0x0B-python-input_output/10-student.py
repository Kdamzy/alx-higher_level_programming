#!/usr/bin/python3
"""Class to JSON"""


class Student:
    """Define a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the body"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
