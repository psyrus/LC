"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""
from typing import List
class Solution:
    # I would have never been able to think of this in 10000 years... No idea why. I just couldn't get how the output needs to be incremented by right ptr - left ptr + 1.
    # How people figure that part out in their heads is beyond me
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        output = 0
        cumulative_val = 1
        l_ptr = 0
        len_nums = len(nums)
        for r_ptr in range(len_nums):
            cumulative_val *= nums[r_ptr]
            while cumulative_val >= k and l_ptr <= r_ptr:
                cumulative_val = cumulative_val / nums[l_ptr]
                l_ptr += 1
            # This happens on each step, so as the size of the acceptable values grows, so each time it increments the counter by a bigger number (n + n-1 + n-2 + n-... etc)
            output += r_ptr - l_ptr + 1
        return output

    def numSubarrayProductLessThanKMemoryOutofBounds(self, nums: List[int], k: int) -> int:
        output = []
        len_nums = len(nums)
        for i in range(len_nums):
            this_output = []
            cumulative_val = nums[i]
            if cumulative_val >= k:
                continue
            this_output.append([cumulative_val])
            for j in range(i + 1, len_nums):
                if cumulative_val * nums[j] >= k:
                    break
                this_output.append(this_output[-1] + [nums[j]])
                cumulative_val *= nums[j]

            output += this_output

        return len(output)


x = Solution()
print(x.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
print(x.numSubarrayProductLessThanK(nums = [1,2,3,4,5], k = 0))
print(x.numSubarrayProductLessThanK(nums = [1,2,3,4,5,6,7], k = 10000))


# 10, 3, 2, 5, 6
# 10, 3, 2 | 10, 3 | 3, 2 | 3, 2, 5 | 2, 5 | 2, 5, 6 | 5, 6 | (an extra 5 for each individual item) -> 12
# L3 = 6, L3 = 6, L3 =