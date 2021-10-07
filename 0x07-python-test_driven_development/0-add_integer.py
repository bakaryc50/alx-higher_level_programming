#!/usr/bin/python3


"""
    0-add_integer module definition
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers
    add_integer(1, 98)
    return 99
    """
    if not isinstance(a, (float, int)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (float, int)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
