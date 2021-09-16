#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    function that returns a list with all values multi by a number.
    """
    if my_list is not None:
        return list(map(lambda val: val * number, my_list))
    return none
