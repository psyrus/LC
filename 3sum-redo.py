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

"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Several ways to do it, but the smartest for 3 sum is as follows:
        # Separate into negatives, zeroes and positives (arrays of each)
        # If there are >= 3 zeroes, that can be an automatic combination
        # If there is at least 1 zero, then check each negative against whether its positive version exists, and if so, add that to output
        # Finally, loop through (positives, then negatives), taking two of each type, and checking if the opposite value of those two values' sum exists, if so - add that to output

        # Another approach is https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
        # Handle it as a super-set to 2 sum
        # Always sort the list of integers first
        # Having them sorted allows you to keep iterating right until you don't have the same value as the previous one, to avoid duplicates
        # The two-sum algorithm is simple, just check if val_l + val_r == target, if so then add to output, then make sure to loop the l index up until the val_l is new (so no duplicates), if < target then l += 1, else r -=1
        # The three sum super set (loop) is what makes the "target" for the twosum, and dictates where l begins
        # Note the extra check such that after the first value, for the 3sum loop we skip an index if its value is the same as the last item in the list (to avoid duplicates again)
        pass

x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))
print(x.threeSum([]))
print(x.threeSum([0]))