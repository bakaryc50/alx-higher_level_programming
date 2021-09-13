#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific position
    @my_list: the list of element
    @idx: index
    @element: element
    Return: the list if failed if idx is negative, if idx is out of range
    """
    if my_list is not None and -1 < idx < len(my_list):
        my_list[idx] = element
    return my_list
