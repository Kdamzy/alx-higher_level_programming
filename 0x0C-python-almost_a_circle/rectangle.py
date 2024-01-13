#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """implement Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set private attribute(__width)"""
        self.validate_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set private attribute(__height)"""
        self.validate_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Return private attribute(__x)"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set private attribute(__x)"""
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Return private attribute(__y)"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set private attribute(__y)"""
        self.validate_int("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.height * self.width)

    def display(self):
        """Prints to stdout the representation of the rectangle"""
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates the arguments props in the class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns a dictionary representation of this class"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def validate_int(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)