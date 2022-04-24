# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class SolutionBruteForce:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []

        l1_iter = 0
        l2_iter = 0
        # First add the items to a singular list while one is larger than the other
        while l1_iter < len(nums1) and l2_iter < len(nums2):
            if nums1[l1_iter] >= nums2[l2_iter]:
                new_list.append(nums2[l2_iter])
                l2_iter += 1
            else:
                new_list.append(nums1[l1_iter])
                l1_iter += 1
        
        # In case anything is remaining, append that to the end 
        if l1_iter < len(nums1):
            new_list += nums1[l1_iter:len(nums1)]
        if l2_iter < len(nums2):
            new_list += nums2[l2_iter:len(nums2)]

        rounded_down_half_way_point = int(len(new_list) / 2)
        median = new_list[rounded_down_half_way_point] if len(new_list) % 2 != 0 else (new_list[rounded_down_half_way_point - 1] + new_list[rounded_down_half_way_point]) / 2
        return float(median)

class SolutionBinarySearch:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1_iter = 0
        l2_iter = 0
        rounded_down_half_way_point = int((len(nums1) + len(nums2)) / 2)
        even_list = (len(nums1) + len(nums2)) % 2 == 0
        cur_val = None
        prev_val = None
        # First add the items to a singular list while one is larger than the other
        while l1_iter + l2_iter < rounded_down_half_way_point + 1:
            prev_val = cur_val
            if l1_iter >= len(nums1):
                cur_val = nums2[l2_iter]
                l2_iter += 1
            elif l2_iter >= len(nums2):
                cur_val = nums1[l1_iter]
                l1_iter += 1
            elif nums1[l1_iter] >= nums2[l2_iter]:
                cur_val = nums2[l2_iter]
                l2_iter += 1
            else:
                cur_val = nums1[l1_iter]
                l1_iter += 1

        median = (cur_val + prev_val) / 2 if even_list else cur_val
        return float(median)

class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
        
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

if __name__ == '__main__':
    x = Solution()
    # print(x.findMedianSortedArrays([2], []))
    # print(x.findMedianSortedArrays([0, 0], [0, 0]))
    # print(x.findMedianSortedArrays([], [2, 3]))
    # print(x.findMedianSortedArrays([1,3], [2]))
    # print(x.findMedianSortedArrays([1,2], [3,4]))
    # print(x.findMedianSortedArrays([1,2], [3,4,5,6,7,8]))
    print(x.findMedianSortedArrays([1,2,3], [10,400,401,600,601, 602, 603]))
    # print(x.findMedianSortedArrays([1,2,10,400,600,603], [3,401,601, 602]))
