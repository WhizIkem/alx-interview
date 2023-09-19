#!/usr/bin/python3
"""
This module contains a function to rotate a given
n x n 2D matrix by 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given matrix by 90 degree clockwise in-place.

    Args:
        matrix: List of lists representing the matrix to rotate.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
