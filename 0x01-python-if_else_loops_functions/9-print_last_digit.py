#!/usr/bin/python3


def print_last_digit(number):
    """ prints the last digit of a number
    and return the value of the last digit
    """
    number = abs(number) % 10
    print("{}".format(number))
    return (int(number))
