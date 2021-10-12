#!/usr/bin/python3
"""
Module for a class that inherits from a list
"""


class MyList(list):
    """Manage a list of integers
    """

    def print_sorted(self):
        """ prints the list in ascending order
        """
        print(sorted(self))
