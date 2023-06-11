#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix = map(lambda ligne: list(map(lambda x: x ** 2, ligne)), matrix)
    return list(matrix)
