#!/usr/bin/python3
""" Provide the rectangle class definition """


from models.base import Base


class Rectangle(Base):
    """ A class that represents Rectangles """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instanciate a class Rectangle """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width():
        """ Get the width value """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set the width value """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height():
        """ Get the height value """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set the height value """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x():
        """ Get the x value """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set the x value """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y():
        """ Get the y value """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set the y value """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ compute the area of the rectangle """
        return self.__width * self.__height
