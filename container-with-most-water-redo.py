"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Look at left and right, calculate area
        # If area goes down, return early?
        l = 0
        r = len(height) - 1

        current_max_area = 0
        while l < r:
            this_area = (r - l) * min(height[r], height[l])
            if this_area > current_max_area:
                current_max_area = this_area

            if height[r] <= height[l]:
                r -= 1
            else:
                l += 1

        return current_max_area

    def maxAreaWrong(self, height: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(height) - 1

        max_r_ptr = r_ptr

        r_max_volume = -1

        while r_ptr > l_ptr:
            this_vol = height[r_ptr] * (r_ptr + 1)
            if this_vol > r_max_volume:
                r_max_volume = this_vol
                max_r_ptr = r_ptr

            r_ptr -= 1

        l_max_volume = -1
        max_l_ptr = l_ptr
        while l_ptr < max_r_ptr:
            this_vol = min(height[max_r_ptr], height[l_ptr]) * (max_r_ptr - l_ptr)
            if this_vol > l_max_volume:
                l_max_volume = this_vol
                max_l_ptr = l_ptr

            l_ptr += 1

        return l_max_volume

x = Solution()

print(x.maxArea([1,2,1]))
print(x.maxArea([1,8,6,2,5,4,8,3,7]))