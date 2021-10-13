#!/usr/bin/python3
"""
Provides a function that write a string to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to text file and returns the nb of characters
    """
    with open(filename, mode="w", encoding="UTF-8") as file:
        return file.write(text)
