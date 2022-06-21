"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""
from typing import List
class Solution:
    def sortFrom(self, nums: List[int], sort_start_idx) -> None:
        for i in range(sort_start_idx, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Search from back for a pair of items such that the left hand item is smaller and switch with it
        swapped_idx = None
        i = len(nums) - 1
        while i > 0:
            # Find the candidate for swapping
            if nums[i - 1] < nums[i]:
                swapped_idx = i - 1
                # Find the lowest number between swapped_idx and the end of the array to swap with
                min_idx = i
                for j in range(i, len(nums)):
                    if nums[j] < nums[min_idx] and nums[j] > nums[swapped_idx]:
                        min_idx = j
                tmp = nums[swapped_idx]
                nums[swapped_idx] = nums[min_idx]
                nums[min_idx] = tmp

                # Then sort everything from the left swapped index to the end in ascending order
                self.sortFrom(nums, swapped_idx + 1)
                break
            i -= 1

        if swapped_idx == None:
            self.sortFrom(nums, 0)

        return nums


if __name__ == '__main__':
    test_cases = [
        [1,3,4,2],
        [1,3,2],
[1,2],
        [1,2,3],
        [3,2,1],
        [1,1,5],
    ]
    correct_answers = [
        [1,4,2,3],
        [2,1,3],
        [2,1],
        [1,3,2],
        [1,2,3],
        [1,5,1],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.nextPermutation(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )

