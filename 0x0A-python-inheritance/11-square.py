#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class body."""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the Square"""
        return f"[Square] {self.__width}/{self.__height}"
