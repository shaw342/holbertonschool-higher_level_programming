#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            if y != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][y]), end='')

        print()
