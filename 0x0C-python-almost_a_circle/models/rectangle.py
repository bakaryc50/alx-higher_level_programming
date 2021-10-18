#!/usr/bin/python3
""" Provide the rectangle class definition """


from models.base import Base


class Rectangle(Base):
    """ A class that represents Rectangles """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instanciate a class Rectangle """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width():
        """ Get the width value """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set the width value """
        self.__width = width

    @property
    def height():
        """ Get the height value """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set the height value """
        self.__height = height

    @property
    def x():
        """ Get the x value """
        return self.__x

    @x.setter
    def x(self, x):
        """ Set the x value """
        self.__x = x

    @property
    def y():
        """ Get the y value """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set the y value """
        self.__y = y
