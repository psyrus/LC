"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # For each "ring", which begins at 0,0 and moves to 1,1 if n = 3 or n = 4, 2,2 if n = 5 or n = 6
        # Loop just the top row of the ring, and for each item from the initial col -> (width - inital col - 2)

        def rotateFourSet(row, col, width):
            if width == 1:
                return
            target_right = (col, row + width - 1)
            target_bottom = (target_right[1], (2 * row) + width - 1 - col)
            target_left = (target_bottom[1], row)
            original = (row, col)
            # take original and push it all the way right
            # the the value that was there and push that all the way down
            # Take the value that was there and push that all the way left
            # take the value that was there and push it all the way up
            prev_val = matrix[row][col]
            for r, c in [target_right, target_bottom, target_left, original]:
                tmp = prev_val
                prev_val = matrix[r][c]
                matrix[r][c] = tmp


        width = len(matrix)
        total_nested_squares = width//2 + (width % 2) * 2
        for i in range(total_nested_squares):
            this_square_width = width - (2*i)
            for col_offset in range(this_square_width - 1):
                this_row = i
                this_col = i + col_offset
                rotateFourSet(this_row, this_col, this_square_width)


x = Solution()
matrix = [[4,8],[3,6]]
x.rotate(matrix)
print(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
x.rotate(matrix)
print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
x.rotate(matrix)
print(matrix)


matrix = [["a","b","c","d", "e"],["f","g","h","i", "j"],["k","l","m","n","o"],["p","q","r","s", "t"], ["u","v","w","x","y"]]
x.rotate(matrix)
print(matrix)
