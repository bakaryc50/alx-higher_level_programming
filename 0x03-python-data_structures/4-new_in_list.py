#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Function that replaces an element in a list without modifying the orginal
    Parameters:
    @my_list: the list
    @idx: the index
    @element:
    Return: the copy of the original if failed
    """
    if my_list is not None and -1 < idx < len(my_list):
        return my_list[:idx] + [element] + my_list[idx+1:]
    return my_list[:]
