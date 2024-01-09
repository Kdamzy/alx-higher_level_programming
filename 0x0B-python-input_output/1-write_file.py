#!/usr/bin/python3
"""Write file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
