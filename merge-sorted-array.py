"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # Edge case handling
        if n == 0:
            return

        # Iterate backwards filling up the nums1 empty part
        nums1_ptr = m - 1
        nums2_ptr = n - 1
        insert_ptr = m + n - 1

        while insert_ptr >= 0:
            nums1_val = nums1[nums1_ptr]
            nums2_val = nums2[nums2_ptr]
            if nums1_ptr >= 0 and nums1_val >= nums2_val:
                nums1[insert_ptr] = nums1_val
                nums1_ptr -= 1
            elif nums2_ptr >= 0:
                nums1[insert_ptr] = nums2_val
                nums2_ptr -= 1

            insert_ptr -= 1
        