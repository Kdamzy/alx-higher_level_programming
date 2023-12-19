#!/usr/bin/python3
# 2-square.py
"""Define a squre."""


class Square:
    """class of the square"""

    def __init__(self, size=0):
        """initialization of the new square
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
