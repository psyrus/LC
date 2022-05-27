"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
from sys import maxsize
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Would probably be useful to have a "visited" hashmap to ensure we don't duplicate values or look at the same island twice
        # Will use also a "seen_this_time" hashmap to not double count squares on the same island

        global_seen = {}
        height = len(grid)
        width = len(grid[0])

        def getLandLength(start_row_idx, start_col_idx):
            if start_row_idx < 0 or start_row_idx >= height or start_col_idx < 0 or start_col_idx >= width:
                return 0

            this_tuple = (start_row_idx, start_col_idx)
            if this_tuple in global_seen:
                return 0

            if grid[start_row_idx][start_col_idx] == 0:
                return 0

            global_seen[this_tuple] = True

            up = getLandLength(start_row_idx + 1, start_col_idx)
            down = getLandLength(start_row_idx - 1, start_col_idx)
            left = getLandLength(start_row_idx, start_col_idx + 1)
            right = getLandLength(start_row_idx, start_col_idx - 1)

            return 1 + up + down + left + right

        max_island_size = 0
        for row_idx in range(height):
            for col_idx in range(width):
                if grid[row_idx][col_idx] == 0:
                    continue
                if (row_idx, col_idx) in global_seen:
                    continue

                max_island_size = max(
                    max_island_size, getLandLength(row_idx, col_idx))

        return max_island_size


x = Solution()

this_grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

# this_grid = [[0,0,0,0,0,0,0,0]]
print(x.maxAreaOfIsland(this_grid))
