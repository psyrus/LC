"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Input: intervals = [[1,4],[0,4]]
Output: [0,4]

Input
[[2,3],[4,5],[6,7],[8,9],[1,10]]
Output
[[1,10],[1,10],[1,10],[1,10]]
Expected
[[1,10]]

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List
class Solution:
    def isOverlapping(self, first:List[int], second:List[int]) -> bool:
        return max(first[0], second[0]) <= min(first[1], second[1])

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        LOWER_BOUND = 0
        UPPER_BOUND = 1

        # It might make sense just to sort the intervals first by start val?
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            # No overlap is defined if the end of x > start of y, and if end of y > start of x
            if intervals[i][LOWER_BOUND] > output[-1][UPPER_BOUND]:
                output.append(intervals[i])
            else:
                output[-1][UPPER_BOUND] = max(intervals[i][UPPER_BOUND], output[-1][UPPER_BOUND])

        return output

