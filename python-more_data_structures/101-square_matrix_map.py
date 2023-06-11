def square_matrix_map(matrix=[]):
    result = map(lambda ligne: list(map(lambda x: x ** 2, ligne)), matrix)
    return list(result)
