"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
# Try and do it in O(N) time
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                squares.append(nums[l] ** 2)
                l += 1
            else:
                squares.append(nums[r] ** 2)
                r -= 1
        # Return the reversed array
        return squares[::-1]
