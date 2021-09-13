#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Function that retrieves an element from a list
    Parameters:
    my_list: the list
    idx: the index
    Return: the element
    """
    if my_list is not None and -1 < idx < len(my_list):
        return my_list[idx]
    return None
