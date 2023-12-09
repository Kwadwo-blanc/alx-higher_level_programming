#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = matrix.copy()

    for row in range(len(matrix)):
        result_matrix[row] = list(map(lambda x: x**2, matrix[row]))

    return result_matrix
