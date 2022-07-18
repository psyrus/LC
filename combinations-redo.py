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

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        def backtrack(count:int, max_num:int, existing_sets: List[List[int]]) -> List[List[int]]:
            if count == 0:
                return existing_sets

            new_level = []
            for i in range(1, max_num + 1):
                for item in existing_sets:
                    if item and i <= item[-1]:
                        continue
                    new_level.append(item + [i])

            return backtrack(count - 1, max_num, new_level)


        return backtrack(count = k, max_num = n, existing_sets = [[]])

# https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination#2.-combination
# I need to be able to understand why that algorithm actually works and makes sense. My way makes sense to me but it is not backtracking...
x = Solution()
print(x.combine(1, 1))
print(x.combine(4, 2))
print(x.combine(4, 3))