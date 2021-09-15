#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    function that replaces all occurences of an elemnt
    @my_list, search, replace:
    Return: new list
    """
    if my_list is not None:
        new_list = [x if x != search else replace for x in my_list]
        return new_list
    return None
