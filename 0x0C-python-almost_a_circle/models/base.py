#!/usr/bin/python3
""" Provide a Base class for all others classes """


class Base():
    """ Base class for all others classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiate a base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
