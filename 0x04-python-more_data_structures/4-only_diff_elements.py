#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    function that returns a set of all elment present in only ones set
    @set_1, set_2
    Return: the set
    """
    if set_1 is not None and set_2 is not None:
        return set_1 ^ set_2
    return None
