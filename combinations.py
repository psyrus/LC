"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]
"""
# Couldn't get it: https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Recursive is way faster! 140ms vs 1200ms
        return self.combineRecursive(n, k)

    def combineRecursive(self, upper_bound: int, digits_to_combine: int) -> List[List[int]]:

        if digits_to_combine == 0:
            return [[]]

        this_iteration = []
        for i in range(digits_to_combine, upper_bound + 1):
            next_combinations = self.combineRecursive(i - 1, digits_to_combine - 1)
            for combo in next_combinations:
                this_iteration.append(combo + [i])

        return this_iteration

    def combineIterative(self, n: int, k: int) -> List[List[int]]:
        output = [[]]

        for i in range(k):
            new_output = []
            for combo in output:
                upper = combo[0] if combo else n + 1
                for j in range(1, upper):
                    new_output.append([j] + combo)

            output = new_output

        return output


x = Solution()
# print(x.combineIterative(3, 2))
print(x.combineRecursive(3, 2))