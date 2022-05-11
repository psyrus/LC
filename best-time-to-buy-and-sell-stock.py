"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l = 0
        r = l + 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)
            r += 1

        return max_profit


if __name__ == '__main__':
    test_cases = [
        [2, 1, 2, 0, 1],
        [2, 1, 4],
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],

    ]
    correct_answers = [
        1,
        3,
        5,
        0,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.maxProfit(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
