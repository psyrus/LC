"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get all rotten orange positions and put them in a stack
        height = len(grid)
        width = len(grid[0])
        rotten_stack = deque([])
        fresh_count = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 2:
                    rotten_stack.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        iterations = 0
        while rotten_stack:
            new_rotten = False
            for _ in range(len(rotten_stack)):
                row, col = rotten_stack.popleft()
                right = (row, col + 1)
                left = (row, col - 1)
                down = (row + 1, col)
                up = (row - 1, col)
                for r, c in [left, right, up, down]:
                    if r < 0 or r >= height:
                        continue
                    if c < 0 or c >= width:
                        continue

                    if grid[r][c] != 1:
                        continue

                    grid[r][c] = 2
                    rotten_stack.append((r,c))
                    new_rotten = True
                    fresh_count -= 1

            if new_rotten:
                iterations += 1

        return iterations if fresh_count == 0 else -1
