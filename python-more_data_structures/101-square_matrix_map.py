def square_matrix_map(matrix=[]):
    result = []
    for i in matrix:
        a = list(map(lambda x: x*x, i))
        result.append(a)

    return result
