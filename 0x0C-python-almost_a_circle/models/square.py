#!/usr/bin/python3
"""Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class body."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a New Square.

        Args:
            size (int): The size of the Square.
            x (int): The x value of the Square.
            y (int): The y value of Square.
            id (int): The id of the Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary rep. of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)