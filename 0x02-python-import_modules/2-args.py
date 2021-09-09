#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    nbargs = len(argv) - 1

    if nbargs == 0:
        print("0 arguments.")
    elif nbargs == 1:
        print("1 argument:")
        print("{}: {}".format(1, argv[nbargs]))
    else:
        print("{} arguments:".format(nbargs))
        for i in range(nbargs):
            print("{}: {}".format(i + 1, argv[i + 1])) 
