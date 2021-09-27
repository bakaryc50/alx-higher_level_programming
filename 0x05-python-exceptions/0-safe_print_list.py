#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list
    @my_list: the list
    """
    try:
        for i in my_list[:x]:
            print(i, end="")
    except:
        print("Can't print an index not found")
