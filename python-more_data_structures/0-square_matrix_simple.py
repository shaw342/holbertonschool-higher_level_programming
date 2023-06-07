#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for i in matrix:
        a = list(map(lambda x: x * x, i))
        result.append(a)
    return result
