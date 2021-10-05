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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        type(self).width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).height = height

    @property
    def width(self):
        """Get width method
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method
        """
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
        type(self).__height = value
