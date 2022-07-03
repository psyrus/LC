"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
    Input: n = 1
    Output: 1
 
Constraints:
    1 <= n <= 9
"""
class Solution:
    def setValues(self, row:int, col:int, val:int) -> None:
        for i in range(len(self.matrix)):
            # 1 out the whole row
            if isinstance(self.matrix[row][i], int):
                self.matrix[row][i] += val
            # 1 out the column
            if isinstance(self.matrix[i][col], int):
                self.matrix[i][col] += val
            # 1 out Top left to bottom right diagonal
            up_left = (row - i, col - i)
            down_right = (row + i, col + i)
            up_right = (row - i, col + i)
            down_left = (row + i, col - i)
            for itr_row, itr_col in [up_left, up_right, down_right, down_left]:
                if 0 <= itr_row < len(self.matrix) and 0 <= itr_col < len(self.matrix) and isinstance(self.matrix[itr_row][itr_col], int):
                    self.matrix[itr_row][itr_col] += val

    def addQueen(self, row:int, col:int) -> None:
        self.matrix[row][col] = "Q"
        self.setValues(row, col, 1)


    def removeQueen(self, row:int, col:int) -> None:
        self.setValues(row, col, -1)
        self.matrix[row][col] = 0


    def isAttackable(self, row:int, col:int) -> bool:
        return self.matrix[row][col] != 0

    def totalNQueens(self, n: int) -> int:
        self.matrix = [[0] * n for i in range(n)]
        def backtrack(row:int, count:int) -> int:

            for col in range(n):
                if self.isAttackable(row, col):
                    continue

                self.addQueen(row, col)
                if row == n - 1:
                    count += 1
                else:
                    count = backtrack(row+1, count)

                self.removeQueen(row, col)

            return count

        return backtrack(0, 0)


x = Solution()
print(x.totalNQueens(9))