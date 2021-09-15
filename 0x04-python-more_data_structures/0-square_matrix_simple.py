#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    matrix that computes the square value of its elements
    @matrix: the matrix parameter
    Return: new matrix
    """
    if matrix is not None:
        new_matrix = list(map(
            lambda row: list(map(lambda x: x ** 2, row
            )), 
            matrix
        ))
        return new_matrix
    return None
