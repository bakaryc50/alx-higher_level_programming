#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values * by 2.
    """
    if a_dictionary is not None:
        return list(map(lambda val: val * 2, a_dictionary))
    return a_dictionary
