"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Iterate left to right, coming up with the sum
        # If there is any number that causes it to go negative, ignore everything to that point and restart the counter
        max_sum = nums[0]
        current_sum = max_sum
        for v in nums[1:]:
            new_sum = current_sum + v
            current_sum = max(v, new_sum)
            max_sum = max(max_sum, current_sum)
        return max_sum
