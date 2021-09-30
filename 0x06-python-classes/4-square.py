#!/usr/bin/python3


""" Module providing a definition of a class 'Square'
"""


class Square():
    """ A class 'Square' that defines a square by based on 0-square
    """
    def __init__(self, size=0):
        """ Instantiation of a Square or initialization
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """Accessing and retrieving the size of the Squre
        """
        return self.__size

    def size(self, value):
        """Setting and updating the size of the Square
        """
        self.__size = value

    def area(self):
        """ Compute the area of the Square
        """
        return self.__size ** 2
