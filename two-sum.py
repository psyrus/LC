from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        srt_arr = sorted(nums)
        # Loop through and compare largest and smallest
        left_offset = 0
        right_offset = -1
        correct_values = []
        while True:
            this_sum = srt_arr[left_offset] + srt_arr[right_offset]
            if this_sum == target:
                correct_values = [srt_arr[left_offset], srt_arr[right_offset]]
                break
            elif this_sum < target:
                left_offset += 1
            else:
                right_offset -= 1
        left_index = nums.index(correct_values[0])
        backwards_iter = len(nums) - 1
        while backwards_iter >= 0:
            if correct_values[1] == nums[backwards_iter]:
                right_index = backwards_iter
                break
            backwards_iter -= 1
        return [left_index, right_index]

if __name__ == '__main__':
    x = Solution()
    print(x.twoSum([-3,4,3,90], 0))