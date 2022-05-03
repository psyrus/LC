# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 3 pointers (l, r, span)
        # if final total > 0, decrement r pointer
        # if final total <= 0, increment l pointer
        l = 0
        output = []
        while l < len(nums) - 2:
            r = len(nums) - 1
            mover = l + 1
            while mover < r:
                sum = nums[r] + nums[l] + nums[mover]
                if sum == 0:
                    sorted_output_item = sorted([nums[r],nums[l],nums[mover]])
                    if sorted_output_item not in output:
                        output.append(sorted_output_item)
                if sum >= 0:
                    r -= 1
                else:
                    mover += 1
            l += 1
        return output


if __name__ == '__main__':
    test_cases = [
        [-2, 0, 1, 1, 2],
        [-1,0,1,2,-1,-4,-2,-3,3,0,4],
        [-1, 0, 1, 2, -1, -4],
        [],
        [0],
    ]
    correct_answers = [
        [[-2, 0, 2], [-2, 1, 1]],
        [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]],
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        [],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.threeSum(t)
        print(
            f"{'Correct' if sorted(my_answer) == sorted(correct_answers[i]) else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
