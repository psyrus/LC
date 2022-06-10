"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""
from typing import List
class Solution:
    def isContained(self, list: List[int], val:int) -> bool:


        return True
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        upper_bound = min(firstList[-1][-1], secondList[-1][-1]) + 1
        lower_bound = max(firstList[0][0], secondList[0][0])

        list1_idx = 0
        list2_idx = 0
        output_idx = 0
        output = [[]]

        for v in range(lower_bound, upper_bound):
            while v > firstList[list1_idx][1] and list1_idx < len(firstList):
                list1_idx += 1

            while v > secondList[list2_idx][1] and list2_idx < len(secondList):
                list2_idx += 1

            if v >= firstList[list1_idx][0] and v >= secondList[list2_idx][0] and v <= firstList[list1_idx][1] and v <= secondList[list2_idx][1]:
                # This is within both the current ranges
                output[output_idx].append(v)
            elif output[output_idx]:
                output_idx += 1
                output.append([])

        return output

x = Solution()
print(x.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))