#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for num, row in enumerate(new_matrix):
        for num2, col in enumerate(new_matrix):
            new_matrix[num][num2] = row[num2] ** 2

    return new_matrix 
