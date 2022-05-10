"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i, n in enumerate(nums):
            if n not in num_pos:
                num_pos[n] = []
            num_pos[n].append(i)
        nums.sort()
        answer = []
        l_ptr = 0
        r_ptr = len(nums) - 1

        while l_ptr < r_ptr:
            this_sum = nums[l_ptr] + nums[r_ptr]

            if this_sum == target:
                answer = [nums[l_ptr], nums[r_ptr]]
                break
            elif this_sum < target:
                l_ptr += 1
            else:
                r_ptr -= 1

        # Normalize answer to original indeces
        answer[0] = num_pos[answer[0]].pop(0)
        answer[1] = num_pos[answer[1]].pop(0)
        return answer