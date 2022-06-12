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
    def render(self, list:List[List[int]], upperbound:int):
        list_idx = 0
        outputstr = ""
        for i in range(0, upperbound):
            if list_idx >= len(list) or i < list[list_idx][0] or i >= list[list_idx][-1]:
                outputstr += "_"
            else:
                outputstr += "□"
            if list_idx < len(list) and i > list[list_idx][-1]:
                list_idx += 1

        print(outputstr)

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        START = 0
        END = -1

        firstlist_idx = 0
        secondlist_idx = 0
        output = []

        # loop until when? We exceed the last element of either list
        while firstlist_idx < len(firstList) and secondlist_idx < len(secondList):

            if firstList[firstlist_idx][END] < secondList[secondlist_idx][START]:
                firstlist_idx += 1
                continue

            if secondList[secondlist_idx][END] < firstList[firstlist_idx][START]:
                secondlist_idx += 1
                continue

            # Check if there is overlap
            output.append([max(firstList[firstlist_idx][START], secondList[secondlist_idx][START]), min(firstList[firstlist_idx][END], secondList[secondlist_idx][END])])

            # Conditions
            first_next_exists = firstlist_idx + 1 < len(firstList)
            second_next_exists = secondlist_idx + 1 < len(secondList)
            first_next_within_current_second = first_next_exists and firstList[firstlist_idx + 1][START] <= secondList[secondlist_idx][END]
            second_next_within_current_first = second_next_exists and secondList[secondlist_idx + 1][START] <= firstList[firstlist_idx][END]

            if first_next_within_current_second or (not second_next_within_current_first and first_next_exists and firstList[firstlist_idx][START] <= secondList[secondlist_idx][START]):
                firstlist_idx += 1
            elif second_next_within_current_first or (not first_next_within_current_second and second_next_exists and secondList[secondlist_idx][START] <= firstList[firstlist_idx][START]):
                secondlist_idx += 1
            else:
                break

        return output

x = Solution()
# print(x.intervalIntersection(,))
print(x.intervalIntersection([[2,3],[4,6],[7,9],[10,16],[17,20]],[[1,3],[4,7],[10,11],[15,18]]))
print(x.intervalIntersection([[10,12],[18,19]],[[1,6],[8,11],[13,17],[19,20]]))
print(x.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
print(x.intervalIntersection([[4,6],[7,8],[10,17]], [[5,10]]))
print(x.intervalIntersection([[8,15]], [[2,6],[8,10],[12,20]]))


