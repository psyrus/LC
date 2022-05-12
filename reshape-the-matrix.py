"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        # Set up new matrix
        output_matrix = [[0 for j in range(c)] for i in range(r)]
        output_row = 0
        output_col = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                output_matrix[output_row][output_col] = mat[i][j]
                output_col += 1
                if output_col == c:
                    output_col = 0
                    output_row += 1
        return output_matrix
