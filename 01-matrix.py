"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
from collections import deque
from typing import List
class Solution:
    # Omg help me I have no idea what I'm doing with BFS: https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        height, width = len(mat), len(mat[0])
        # Somehow people know that we need breadth first search (BFS)
        # This involves a queue

        my_queue = deque()
        # First do a single pass on each cell, setting the NON 0 cells to -1 (to indicate that they haven't been processed yet) and any zero cells get added to the queue
        for row_idx in range(height):
            for col_idx in range(width):
                if mat[row_idx][col_idx] == 0:
                    my_queue.append((row_idx, col_idx))
                else:
                    mat[row_idx][col_idx] = -1

        # Next loop while there are still items in the queue.
        # On each iteration check the left/right/up/down squares (check_square). Start from the ORIGINAL top left which means popping from the front of the queue
        # If the check square is valid (not out of bounds) and is a -1 (aka a square that needs distance check) then set that check_square = current queue item value + 1
        # Then add the check_square back to the queue
        while my_queue:
            row, col = my_queue.popleft() # To get the deepest item in the queue (first)
            left = (row, col - 1)
            right = (row, col + 1)
            up = (row - 1, col)
            down = (row + 1, col)
            for coords in [left, right, up, down]:
                c_row = coords[0]
                c_col = coords[1]
                if c_row < 0 or c_row >= height or c_col < 0 or c_col >= width:
                    continue
                if mat[c_row][c_col] != -1:
                    continue

                mat[c_row][c_col] = mat[row][col] + 1
                my_queue.append((c_row, c_col))


        return mat

x = Solution()
print(x.updateMatrix([[0,0,0],[0,1,0],[1,1,0]]))
print(x.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(x.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))