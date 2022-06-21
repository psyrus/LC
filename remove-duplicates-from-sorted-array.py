"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        swap_idx = 1
        prev_val = nums[0]
        for idx, val in enumerate(nums):
            if val > prev_val:
                if swap_idx < idx:
                    nums[idx] = nums[swap_idx]
                    nums[swap_idx] = val
                prev_val = val
                swap_idx += 1
        return swap_idx

if __name__ == '__main__':
    test_cases = [
        [0,0,1,1,1,2,2,3,3,4],
        [1,1,2],
        [1],
    ]
    correct_answers = [
        5,
        2,
        1,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.removeDuplicates(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
