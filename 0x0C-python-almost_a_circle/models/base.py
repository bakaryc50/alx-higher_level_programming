#!/usr/bin/python3
""" Provide a class Base fonctionnality """


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class initialization function """
        if id is not None:
            self.id = id
        __nb_objects += 1
        self.id = __nb_objects
