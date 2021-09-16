#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    function that replaces or adds key/value in a dictionary.
    """
    if a_dictionary is not None:
        a_dictionary[key] = value
    return a_dictionary
