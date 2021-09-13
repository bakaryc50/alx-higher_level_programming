#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Function that retrieves an element from a list
    Parameters:
    my_list: the list
    idx: the index
    Return: the element
    """
    if my_list:
        if idx < 0 or idx > len(my_list):
            return "None"
        else:
            return my_list[idx]
