#!/usr/bin/python3
"""
Profived a function that return the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Get a JSON representation of an object
    """
    return json.dumps(my_obj)
