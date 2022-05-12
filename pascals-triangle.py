"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            this_row = []
            prev = 0
            for j in range(len(output[i - 1])):
                val = prev + output[i - 1][j]
                this_row.append(val)
                prev = output[i - 1][j]

            this_row.append(1)
            output.append(this_row)
        return output

if __name__ == '__main__':
    x = Solution()
    x.generate(5)