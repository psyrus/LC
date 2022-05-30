"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

mval = 7
7 > target
7 > nums[0]
7 > nums[-1]
target < nums[-1]
target < nums[0]

Need to shift search area to between mid and nums[-1]

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

"""
Scenarios
mval > target
-------
is nums[r] > target? -> search right side
is nums


"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Log n complexity means a binary search
        # Because the "pivot" point is not at 0, we need to keep in account the wraparound values when moving the "mid"

        l = 0
        r = len(nums) - 1
        output = -1
        while l <= r:
            mid = (l + r) // 2

            val_at_mid = nums[mid]

            if val_at_mid == target:
                output = mid
                return output
            elif val_at_mid < target:
                if nums[r] >= target or val_at_mid > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif val_at_mid > target:
                if nums[l] <= target or val_at_mid < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return output

x = Solution()
print(x.search([4,5,6,7,8,1,2,3], 8))
print(x.search([5,1,2,3,4], 1))