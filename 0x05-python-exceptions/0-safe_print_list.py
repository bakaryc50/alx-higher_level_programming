#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list
    @my_list: the list
    """
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        return x
    finally:
        print()
