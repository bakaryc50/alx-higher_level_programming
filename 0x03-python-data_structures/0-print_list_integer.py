#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    print_list_integer - prints all integers of a list
    Parameter: my_list0-print_list_integer.py
    """
    if my_list:
        print('\n'.join(['{:d}'.format(i) for i in my_list]))
