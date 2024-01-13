#!/usr/bin/python3
"""Base class"""
import json
import turtle
import csv


class Base:
    """Base model Private Class Attributes:
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Id in a constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string rep. of a dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string rep to a file."""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
            
    @staticmethod
    def from_json_string(json_string):
        """Return the list of Json string rep."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                jdata = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in jdata]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize instances to CSV and write """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    sizes = ["id", "width", "height", "x", "y"]
                else:
                    sizes = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, sizes=sizes)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serialize and deserialize in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    size = ["id", "width", "height", "x", "y"]
                else:
                    size = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, size=size)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle graphics module.
        """
        kenny = turtle.Turtle()
        kenny.screen.bgcolor("#b7312c")
        kenny.pensize(3)
        kenny.shape("turtle")

        for rectangle in list_rectangles:
            kenny.showturtle()
            kenny.up()
            kenny.goto(rectangle.x, rectangle.y)
            kenny.down()
            kenny.color("green")
            kenny.begin_fill()
            for _ in range(2):
                kenny.forward(rectangle.width)
                kenny.left(90)
                kenny.forward(rectangle.height)
                kenny.left(90)
            kenny.end_fill()
            kenny.hideturtle()

        for square in list_squares:
            kenny.showturtle()
            kenny.up()
            kenny.goto(square.x, square.y)
            kenny.down()
            kenny.color("blue")
            kenny.begin_fill()
            for _ in range(4):
                kenny.forward(square.size)
                kenny.left(90)
            kenny.end_fill()
            kenny.hideturtle()

        kenny.exitonclick()