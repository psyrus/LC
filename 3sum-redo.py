"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Screwed it up the first time, got too complicated.
        # Don't do two pointer with both upper and lower bound being messed with - Keep the upper bound stable on the outer loop
        # Mess with mid & right in the inner loop

        nums.sort()
        output = []
        len_nums = len(nums)

        #TODO: Need to implement this one again because I suck

        return output

x = Solution()

print(x.threeSum([-2,0,1,1,2]))
print(x.threeSum([0,0,0]))
print(x.threeSum([-1,0,1,2,-1,-4]))
print(x.threeSum([]))
print(x.threeSum([0]))

