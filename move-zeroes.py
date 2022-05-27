"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        for idx in range(len(nums)):
            if nums[idx] == 0:
                # Find the first non-zero value
                non_zero_found = False
                for i in range(idx+1, len(nums)):
                    if nums[i] != 0:
                        non_zero_found = True
                        tmp = nums[idx]
                        nums[idx] = nums[i]
                        nums[i] = tmp
                        break
                # If no non zero was found after this zero, it means there is nothing left to swap!
                if non_zero_found == False:
                    return

if __name__ == '__main__':
    test_cases = [
        [0,1,0,3,12]

    ]
    correct_answers = [
        [1,3,12,0,0]
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.moveZeroes(t)
        print(
            f"{'Correct' if t == correct_answers[i] else 'Wrong'} : {t} ({correct_answers[i]})"
        )
