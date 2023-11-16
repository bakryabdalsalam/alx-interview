#!/usr/bin/python3
"""
creat the function rotate_2d_matrix
"""
def rotate_2d_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save top
            top = matrix[layer][i]

            # Move left to top
            matrix[layer][i] = matrix[-i - 1][layer]

            # Move bottom to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # Move right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # Move top to right
            matrix[i][-layer - 1] = top