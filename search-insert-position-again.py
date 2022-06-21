"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # log n dictates a binary search approach

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return l

if __name__ == '__main__':
    test_cases = [
        ([1,3,5,6], 5),
        ([1,3,5,6], 2),
        ([1,3,5,6], 7),
    ]
    correct_answers = [
        2,
        1,
        4,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.searchInsert(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
