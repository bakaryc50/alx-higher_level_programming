#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    function that replaces or adds key/value in a dictionary.
    """
    if a_dictionary is not None:
        try:
            del a_dictionary[key]
        except KeyError:
            pass
        return a_dictionary
    return None
