"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def permute_helper(need_to_permute:List[int], current_combination):
            if len(need_to_permute) == 0:
                output.append(current_combination)
                return

            for i in range(len(need_to_permute)):
                permute_helper(need_to_permute[:i] + need_to_permute[i + 1:], current_combination + [need_to_permute[i]])

        permute_helper(nums, [])

        return output

x = Solution()
print(x.permute(["a","b","c"]))