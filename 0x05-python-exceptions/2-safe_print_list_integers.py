#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints x elements of a list and only integers
    @my_list: the list
    """
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
    except (ValueError, TypeError):
        pass
    else:
        count += 1
    print()
    return count
