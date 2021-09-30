#!/usr/bin/python3


""" Module providing a definition of a class 'Square'
"""


class Square():
    """ A class 'Square' that defines a square by based on 0-square
    """
    def __init__(self, size=0):
        """ Instantiation of a Square or initialization
        """
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            try:
                if (size < 0):
                    raise ValueError
            except ValueError:
                raise ValueError("size must be >= 0")
