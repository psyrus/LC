"""
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
from collections import deque
from typing import List
class Solution:
    def sortSubArrays(self, sub_list1:List[int], sub_list2:List[int]) -> List[int]:
        l = 0
        r = 0
        output = []
        while l < len(sub_list1) and r < len(sub_list2):
            if sub_list1[l] <= sub_list2[r]:
                output.append(sub_list1[l])
                l += 1
            else:
                output.append(sub_list2[r])
                r += 1

        if l < len(sub_list1):
            output.extend(sub_list1[l:])
        elif r < len(sub_list2):
            output.extend(sub_list2[r:])

        return output


    def sortArray(self, nums: List[int]) -> List[int]:
        # Do it iteratively (bottom up)

        len_nums = len(nums)
        if len_nums < 2:
            return nums

        my_queue = deque([[i] for i in nums])

        while len(my_queue) > 1:
            left = my_queue.popleft()
            right = [] if not my_queue else my_queue.popleft()
            my_queue.append(self.sortSubArrays(left, right))

        return my_queue.pop()