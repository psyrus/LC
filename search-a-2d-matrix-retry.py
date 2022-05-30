"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
from typing import List
class Solution:
    def getNormalizedIndex(self, row:int, col:int, width:int) -> int:
        return row * width + col

    def getRowCol(self, normalized_idx:int, width:int) -> tuple:
        return (normalized_idx // width, normalized_idx % width)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        height = len(matrix)
        width = len(matrix[0])
        l = 0
        r = self.getNormalizedIndex(height - 1, width - 1, width)

        while l <= r:
            mid = (l + r) // 2
            mid_row, mid_col = self.getRowCol(mid, width)
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1


        return False

x = Solution()

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
    ]
target = 53

print(x.searchMatrix(matrix, target))