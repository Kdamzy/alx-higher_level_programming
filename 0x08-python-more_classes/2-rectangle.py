#!/usr/bin/python3
"""
class that define a Rectangle.
"""


class Rectangle:
    """Class of Rectangle defined by width and height
    """

    def __init__(self, width= 0, height= 0):
        """initialise the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the format for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
