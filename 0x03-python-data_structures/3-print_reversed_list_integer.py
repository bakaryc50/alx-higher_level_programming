#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - prints all integers of a list in reverse
    Parameter: my_list
    """
    if my_list:
        print('\n'.join(['{:d}'.format(i) for i in reversed(my_list)]))
