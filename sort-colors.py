"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Just count the number of 1, 2, 3 then modify the nums to be that
        counts = [0, 0, 0]

        for v in nums:
            counts[v] += 1

        idx = 0
        for val, count in enumerate(counts):
            itr = 0
            while itr < count:
                nums[idx] = val
                itr += 1
                idx += 1

        return nums

    def sortColorsConstantSpace(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1

        min_swap_point = l
        max_swap_point = r
        total_iterations = 0
        while l < r:
            total_iterations += 1
            while nums[l] == 0:
                min_swap_point += 1
                l += 1
            while nums[r] == 2:
                max_swap_point -= 1
                r -= 1

            if nums[l] > nums[r]:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp

                l += 1
                r -= 1

        print(total_iterations)
        return nums

x = Solution()
print(x.sortColors([2,2,2,2,2,2,1,1,2]))