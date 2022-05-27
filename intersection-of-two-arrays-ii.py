"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        nums1_ptr = 0
        nums2_ptr = 0
        output = []
        while nums1_ptr < len(nums1) and nums2_ptr < len(nums2):
            try:
                nums2_ptr = nums2.index(nums1[nums1_ptr], nums2_ptr, len(nums2)) + 1
                output.append(nums1[nums1_ptr])
            except ValueError:
                pass
            nums1_ptr += 1


        return output