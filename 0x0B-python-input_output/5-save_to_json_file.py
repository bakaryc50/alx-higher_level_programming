#!/usr/bin/python3
"""Provides a function that write an object to a text file using JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Save an object to a text using JSON representation"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return json.dump(my_obj, f)
