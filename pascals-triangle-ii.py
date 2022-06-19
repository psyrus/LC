"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current_row = [0] * (rowIndex + 1)

        while current_row[-1] != 1:
            prev_row = current_row.copy()

            loop_idx = 0
            while loop_idx < rowIndex + 1 and prev_row[loop_idx] != 0:
                if loop_idx > 0:
                    current_row[loop_idx] = prev_row[loop_idx] + prev_row[loop_idx - 1]
                loop_idx += 1

            current_row[loop_idx] = 1

        return current_row