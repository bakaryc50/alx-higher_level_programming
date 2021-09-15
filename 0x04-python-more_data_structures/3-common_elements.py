#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    function that returns a set of common elements in 2 sets
    @my_list
    Return: the set
    """
    if set_1 is not None and set_2 is not None:
        return set_1 & set_2
    return None
