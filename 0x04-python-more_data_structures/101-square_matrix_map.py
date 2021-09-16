#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    function compute by 2 the values of the matrix
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
