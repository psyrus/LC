"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""
import enum
from typing import List
class Solution:
    def checkRowValid(self, board: List[List[str]], row: int) -> bool:
        value_exists = {}
        for col_idx in range(len(board)):
            val = board[row][col_idx]
            if val == ".":
                continue
            if val in value_exists:
                return False
            else:
                value_exists[val] = True
        return True

    def checkColumnValid(self, board: List[List[str]], col:int) -> bool:
        value_exists = {}
        for row_idx in range(len(board)):
            val = board[row_idx][col]
            if val == ".":
                continue
            if val in value_exists:
                return False
            else:
                value_exists[val] = True
        return True

    def checkGridDuplicates(self, board: List[List[str]], row: int, col:int) -> bool:
        value_exists = {}
        for row_idx in range(row, row + 3):
            for col_idx in range(col, col + 3):
                val = board[row_idx][col_idx]
                if val == ".":
                    continue
                if val in value_exists:
                    return False
                else:
                    value_exists[val] = True
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for idx in range(len(board)):
            if not self.checkRowValid(board, idx):
                return False

            if not self.checkColumnValid(board, idx):
                return False

        for subgrid_start_row in range(0, len(board), 3):
            for subgrid_start_col in range(0, len(board), 3):
                if not self.checkGridDuplicates(board, subgrid_start_row, subgrid_start_col):
                    return False

        return True

if __name__ == '__main__':
    test_cases = [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", "3", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    ]
    correct_answers = [
        True
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.isValidSudoku(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
