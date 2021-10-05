#!/usr/bin/python3


""" Module providing a definition of a class 'Rectangle'
"""


class Rectangle():
    """
    A class Rectangle definition based on 2-rectangle.py
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height method
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ a toString method to print like print()
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            hashes = '#' * self.__width
            return '\n'.join(hashes for h in range(self.__height))
