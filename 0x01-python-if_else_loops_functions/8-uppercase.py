#!/usr/bin/python3


def uppercase(str):
    """ prints a string in uppercase """
    print("{}".format(str.translate(
        {(c | 32): c for c in range(ord('A'), ord('Z') + 1)}
    )))
