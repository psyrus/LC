"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Start L & R on the 0 mark
        # shift R forwards until the total >= target or end of array (Take note of the distance between R - L + 1)
        # Then shift L forwards until total < target or end of array -> Repeat from step 2
        len_nums = len(nums)
        min_length = len_nums + 1
        l = 0
        r = 0
        running_sum = nums[0]
        while l <= r and l < len_nums and r < len_nums:
            if running_sum < target:
                r += 1
                if r < len_nums:
                    running_sum += nums[r]

            else:
                min_length = min(min_length, r - l + 1)
                running_sum -= nums[l]
                l += 1

        return min_length if min_length < len_nums + 1 else 0

x = Solution()
print(x.minSubArrayLen(15, [1,2,3,4,5]))
print(x.minSubArrayLen(7, [2,3,1,2,4,3]))
print(x.minSubArrayLen(target = 4, nums = [1,4,4]))
print(x.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))