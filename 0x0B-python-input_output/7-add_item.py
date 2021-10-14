#!/usr/bin/python3
"""Provides a script that adds all args to a python list"""

from sys import argv


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        save_to_json_file(load_from_json_file(FILENAME) + argv[1:], FILENAME)
    except (FileNotFoundError, ValueError):
        save_to_json_file(argv[1:], FILENAME)
