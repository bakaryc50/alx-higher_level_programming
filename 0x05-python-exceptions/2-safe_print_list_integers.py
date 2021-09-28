#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints x elements of a list and only integers
    @my_list: the list
    """
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        return x
    except ValueError:
        print("not an integer value")
    except IndexError:
        print("IndexError: list index out of range")
    finally:
        print()
