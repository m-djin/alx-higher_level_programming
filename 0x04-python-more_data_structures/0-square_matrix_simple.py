#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = [row[:] for row in matrix]
    for idx, row in enumerate(new_mat):
        for idx2, col in enumerate(new_mat):
            new_mat[idx][idx2] = row[idx2] ** 2
    return new_mat
