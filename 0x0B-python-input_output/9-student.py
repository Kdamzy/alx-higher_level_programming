#!/usr/bin/python3
"""Class to JSON"""


class Student:
    """Define a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the body"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
