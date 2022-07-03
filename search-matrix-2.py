"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = 0
        COL = 1

        def search(matrix: List[List[int]], target: int, top_left_tpl:tuple, bottom_right_tpl:tuple) -> bool:
            # Divide and conquer
            # Base case should be if the sub matrix is only 1 width/height

            midpoint_tpl = ((bottom_right_tpl[ROW] + top_left_tpl[ROW]) // 2, (bottom_right_tpl[COL] + top_left_tpl[COL]) // 2)
            if matrix[midpoint_tpl[ROW]][midpoint_tpl[COL]] == target:
                return True

            # In this case there is only 1 value in the matrix and it wasn't the target as per the previous if statement
            height = bottom_right_tpl[ROW] - top_left_tpl[ROW] + 1
            width = bottom_right_tpl[COL] - top_left_tpl[COL] + 1
            if width < 2 and height < 2 or width < 1 or height < 1:
                return False
            # Divide by the midpoint - Either top/left for mid > than target, bottom/right if mid < target

            if matrix[midpoint_tpl[ROW]][midpoint_tpl[COL]] > target:

                # Top
                top_modifier = (midpoint_tpl[ROW] - 1, bottom_right_tpl[COL])
                t = search(matrix, target, top_left_tpl, top_modifier)

                # Left
                left_top = (midpoint_tpl[ROW], top_left_tpl[COL])
                left_bottom = (bottom_right_tpl[ROW], midpoint_tpl[COL] - 1)
                l = search(matrix, target, left_top, left_bottom)
                return t or l
            else:
                # Bottom
                bottom_modifier = (midpoint_tpl[ROW] + 1, top_left_tpl[COL])
                b = search(matrix, target, bottom_modifier, bottom_right_tpl)

                #Right
                right_top = (top_left_tpl[ROW], midpoint_tpl[COL] + 1)
                right_bottom = (midpoint_tpl[ROW], bottom_right_tpl[COL])
                r = search(matrix, target, right_top, right_bottom)

                return b or r


        return search(matrix, target, (0,0), (len(matrix) - 1, len(matrix[ROW]) - 1))

x = Solution()

print(x.searchMatrix(matrix = [[-1,3]], target = -33))
print(x.searchMatrix(matrix = [[-5]], target = 5))
print(x.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
print(x.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))