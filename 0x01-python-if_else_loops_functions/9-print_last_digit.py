#!/usr/bin/python3


def print_last_digit(number):
    return ((abs(number) % 10) * (-1) ** (number < 0))
