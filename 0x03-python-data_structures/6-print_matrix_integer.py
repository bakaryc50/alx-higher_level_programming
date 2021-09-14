#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Function that prints a matrix of integers
    Parameters:
    @matrix: the matrix
    """
    if matrix is not None:
        for i in matrix:
            for j in i:
                print("{} {}".format(i, j))
    return None
