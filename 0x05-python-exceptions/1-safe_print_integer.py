#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints an integer with {:d}.format
    @my_list: a value
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
    finally:
        print()
