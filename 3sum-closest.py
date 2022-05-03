# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = None
        closest_diff = None
        for l in range(len(nums) - 1):
            r = len(nums) - 1
            mover = l + 1
            while mover < r:
                total = nums[l] + nums[r] + nums[mover]
                this_diff = abs(total - target)
                if None == closest_diff or abs(this_diff) < abs(closest_diff):
                    closest_sum = total
                    closest_diff = this_diff

                if total == target:
                    return closest_sum
                if total > target:
                    r -= 1
                else:
                    mover += 1

        return closest_sum


if __name__ == '__main__':
    test_cases = [
        ([0, 2, 1, -3], 1),
        ([1, 1, -1, -1, 3], -1),
        ([1, 1, -1, -1, 3], 1),
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([0, 1, 2], 0),
    ]
    correct_answers = [
        0,
        -1,
        1,
        2,
        0,
        3,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.threeSumClosest(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
