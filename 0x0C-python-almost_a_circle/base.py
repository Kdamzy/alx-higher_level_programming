#!/usr/bin/python3
"""Base class"""
import json
import turtle
import cvs


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
