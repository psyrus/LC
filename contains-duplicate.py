"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}

        for n in nums:
            if n in num_counts:
                return True
            else:
                num_counts[n] = True

        return False