#!/usr/bin/python3


""" Module providing a definition of a class 'Rectangle'
"""


class Rectangle():
    """
    A class Rectangle definition based on 8-rectangle.py
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ A class instantiation or initialization
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        r1 = rect_1.width * rect_1.height
        r2 = rect_2.width * rect_2.height
        return (rect_1 if r1 > r2 or r1 == r2 else rect_2)

    def square(cls, size=0):
        """creates new instance with height and width == size
        """
        return cls(size, size)

    def __str__(self):
        """ a toString method to print like print()
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            hashes = "{}".format(self.print_symbol) * self.__width
            return '\n'.join(hashes for h in range(self.__height))

    def __repr__(self):
        """ rectangle to be able to recreate a new instance
        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ deletion of an Rectangle
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
