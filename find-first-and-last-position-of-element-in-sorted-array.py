"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
from typing import List
class Solution:
    def searchRangeTwoPointer(self, nums: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(nums) - 1

        output = [-1, -1]

        while l_ptr <= r_ptr and len(nums) > 0 and (output[0] == -1 or output[1] == -1):
            if output[0] == -1:
                if nums[l_ptr] == target:
                    output[0] = l_ptr
                else:
                    l_ptr += 1
            if output[1] == -1:
                if nums[r_ptr] == target:
                    output[1] = r_ptr
                else:
                    r_ptr -= 1

        return output

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Must run O(log N) so obviously must be some kind of binary based approach
        # To check left, we need to make sure that the item at i-1 is not the same (or that i == 0)
        # To check right, we need to make sure that the item at i+1 is not the same (or that i == len(nums) - 1)
        if not nums:
            return [-1, -1]
        def binaryTraverse(left, right, target, neighbor_check_modifier):
            if -1 in [left, right] or (left == right and nums[left] != target):
                return -1
            mid = (left + right) // 2

            if target == nums[mid]:
                neighbour_idx = mid + neighbor_check_modifier
                if neighbour_idx < 0 or neighbour_idx >= len(nums):
                    return mid

                if nums[neighbour_idx] == target:
                    # Not valid because we are not at the outermost position
                    # Need to keep binary searching
                    left = mid + 1 if neighbor_check_modifier > 0 else left
                    right = mid - 1 if neighbor_check_modifier < 0 else right
                else:
                    return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            return binaryTraverse(left, right, target, neighbor_check_modifier)

        left_min = binaryTraverse(0, len(nums) - 1, target, -1)
        right_max = binaryTraverse(left_min, len(nums) - 1, target, 1)

        return [left_min, right_max]

x = Solution()
print(x.searchRange([5,7,7,8,8,10], 8))
print(x.searchRange([], 0))
print(x.searchRange([1], 0))