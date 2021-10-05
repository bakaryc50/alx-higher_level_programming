#!/usr/bin/python3


""" Module providing a definition of a class 'Rectangle'
"""


class Rectangle():
    """
    A class Rectangle definition based on 0-rectangle.py
    """
    def __init__(self, width=0, height=0):
        """ A class instantiation or initialization
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        type(self).__width = value

    @property
    def height(self):
        """Get height method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        type(self).__height = value
