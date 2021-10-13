#!/usr/bin/python3
"""
Provides a function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string to text file and returns the nb of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        return file.write(text)
