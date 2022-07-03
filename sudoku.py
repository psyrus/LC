"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List
class Solution:
    GRID_SIZE = 9

    def findNextEmptyLocation(self) -> tuple[int, int]:
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.board[i][j] == ".":
                    return (i, j)

        return None

    def isRowValid(self, row:int, new_num:str) -> bool:
        for i in range(self.GRID_SIZE):
            if self.board[row][i] == new_num:
                return False

        return True

    def isColValid(self, col:int, new_num:str) -> bool:
        for i in range(self.GRID_SIZE):
            if self.board[i][col] == new_num:
                return False

        return True

    def isBoxValid(self, row:int, col:int, new_num:str) -> bool:
        # Determine which box we are in - 9 items per box, each box is 3x3
        # Can use the division // concept to determine the box and from there, know the initial start point
        # loop from top left to bottom right

        box_row = row // 3
        box_col = col // 3

        start_pos_row = 3 * box_row
        start_pos_col = 3 * box_col

        for i in range(start_pos_row, start_pos_row + 3):
            for j in range(start_pos_col, start_pos_col + 3):
                if self.board[i][j] == new_num: return False

        return True

    def checkValid(self, row:int, col:int, new_num:str):
        return (self.isRowValid(row, new_num) and
               self.isColValid(col, new_num) and
               self.isBoxValid(row, col, new_num))

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        def backtrack() -> bool:
            empty_location = self.findNextEmptyLocation()

            if not empty_location:
                return True

            row, col = empty_location

            for num in range(1, 10):
                candidate = str(num)
                if not self.checkValid(row, col, candidate):
                    continue

                self.board[row][col] = candidate

                if backtrack():
                    return True

                self.board[row][col] = "."

            return False

        backtrack()








x = Solution()
matrix = [
    ["8",".",".",".",".",".",".",".","."],
    [".",".","3","6",".",".",".",".","."],
    [".","7",".",".","9",".","2",".","."],
    [".","5",".",".",".","7",".",".","."],
    [".",".",".",".","4","5","7",".","."],
    [".",".",".","1",".",".",".","3","."],
    [".",".","1",".",".",".",".","6","8"],
    [".",".","8","5",".",".",".","1","."],
    [".","9",".",".",".",".","4",".","."],
    ]
x.solveSudoku(matrix)
print(matrix)