#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    function that returns a list with all values multi by a number.
    """
    return None if my_list is None else list(map(lambda x: x * number, my_list))
