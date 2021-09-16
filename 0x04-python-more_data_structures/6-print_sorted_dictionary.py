#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.
    """
    if a_dictionary is not None:
        for k, v in sorted(a_dictionary.items()):
            print("{}: {}".format(k, v))
    return None
