"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def traverseIsland(row:int, col:int):
            # Need return condition
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            traverseIsland(row - 1, col)
            traverseIsland(row + 1, col)
            traverseIsland(row, col - 1)
            traverseIsland(row, col + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    traverseIsland(i, j)
                    num_islands += 1

        return num_islands