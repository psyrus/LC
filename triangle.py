"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""
from typing import List
class Solution:
    # Iterative stolen from leetcode < Should understand this
    #time O(n^2) space O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Make an array that is as long as the number of rows of the triangle + 1, this will hold the minimum distance to the bottom of that row
        table = [0]*(len(triangle)+1)

        # Loop through the triangle rows *backwards* (bottom to top)
        for row in triangle[::-1]:
            # For each value on the row, check the current minimums in "table". See if the left or right is smaller (from previous lower row) and add that to the traversal
            for i, num in enumerate(row):
                table[i] = num + min(table[i], table[i+1])
        return table[0]

    def minimumTotalRecurse(self, triangle: List[List[int]]) -> int:
        # This is seemingly a DFS issue with a semi tree structure (except that there are connections both left and right)
        # Useful to use memoization so that if a path has already been traversed we know what its min value will be through lookup
        list_len = len(triangle)
        min_to_bottom = {}
        def traverse(row, col):
            # Break case: if row = len of the list
            if row == list_len - 1:
                return triangle[row][col]

            # Recurse condition: Check the min value of looking left, and then looking right
            # It should refer to memoizied values as soon as possible (use backtracking)
            this_pos = (row, col)
            if not this_pos in min_to_bottom:
                left_traverse = traverse(row + 1, col)
                right_traverse = traverse(row + 1, col + 1)
                min_to_bottom[this_pos] = triangle[row][col] + min(left_traverse, right_traverse)

            return min_to_bottom[this_pos]

        return traverse(0, 0)

x = Solution()
print(x.minimumTotal([[2],[9,4],[9,5,7],[9,9,8,3]]))
print(x.minimumTotal([[-10]]))
print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))