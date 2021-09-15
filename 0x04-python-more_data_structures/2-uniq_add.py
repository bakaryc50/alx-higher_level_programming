#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a list
    @my_list
    Return: the result
    """
    if my_list is not None:
        result = sum(set(my_list))
        return result
    return None
