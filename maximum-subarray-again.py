"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i, v in enumerate(nums[1:]):
            current_sum = max(current_sum, 0) + v
            max_sum = max(current_sum, max_sum)
        return max_sum

if __name__ == '__main__':
    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
    ]
    correct_answers = [
        6,
        1,
        23
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.maxSubArray(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
