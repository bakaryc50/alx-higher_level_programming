#!/usr/bin/python3
"""Provides a function to create an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, mode="r", encoding="UTF-8") as file:
        return json.load(file)
