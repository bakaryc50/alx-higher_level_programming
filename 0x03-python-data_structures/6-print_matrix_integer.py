#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Function that prints a matrix of integers
    Parameters:
    @matrix: the matrix
    """
    if matrix is not None:
        print('\n'.join([
            ' '.join(['{:d}'.format(x) for x in y]) for y in matrix
            ]))
    return None
