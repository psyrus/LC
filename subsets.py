"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recurse(nums_subset:List[int]) -> List[List[int]]:
            if not nums_subset:
                return [[]]

            next_level = recurse(nums_subset[:-1])
            return next_level + [[nums_subset[-1]] + i for i in next_level]

        return recurse(nums)


x = Solution()
print(x.subsets([1,2,3]))
print(x.subsets([1,2,3,4]))
print(x.subsets([0]))