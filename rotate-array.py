"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Reduce inefficiency by ensuring k wraparound
        k = k % len(nums)
        tmp_arr = [0 for i in nums]

        for i in range(len(nums)):
            # Get new position
            new_i = (i + k) % len(nums)
            tmp_arr[new_i] = nums[i]

        for i in range(len(nums)):
            nums[i] = tmp_arr[i]
