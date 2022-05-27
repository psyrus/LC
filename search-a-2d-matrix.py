"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
from typing import List
class Solution:
    def convertToPosition(self, linear_idx, matrix):
        cols = len(matrix[0])

        row_idx = linear_idx // cols
        col_idx = linear_idx % cols
        return [row_idx, col_idx]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Create a function that maps a linear index to the position in the matrix
        # That way I can just use a normal binary search to figure out if the target exists

        l = 0
        r = len(matrix) * len(matrix[0])
        if r == 1:
            return matrix[0][0] == target

        # temp = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         temp.append(matrix[i][j])

        while l < r:
            mid = (l + r) // 2

            mid_pos = self.convertToPosition(mid, matrix)
            val_mid = matrix[mid_pos[0]][mid_pos[1]]
            # val_mid = temp[mid]
            if val_mid == target:
                return True
            elif val_mid < target:
                l = mid + 1
            else:
                r = mid

        return False

if __name__ == '__main__':
    test_cases = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
        ([[1,1]], 2),
        ([[1]], 2),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    ]
    correct_answers = [
        True,
        False,
        False,
        False
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.searchMatrix(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
