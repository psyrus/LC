from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start from edges, take that as baseline
        # from both sides iterate until you find an item with a height > than the current one and test that

        left_iter = 0
        right_iter = len(height) - 1

        max_area = min(height[left_iter], height[right_iter]) * (right_iter - left_iter)
        while left_iter < right_iter:
            this_area = min(height[left_iter], height[right_iter]) * (right_iter - left_iter)
            if this_area > max_area:
                max_area = this_area

            if height[left_iter] < height[right_iter]:
                left_iter += 1
            else:
                right_iter -= 1
        return max_area

    def maxAreaBruteForce(self, height: List[int]) -> int:

        max_found = 0
        for idx, h in enumerate(height):
            for j in range(idx + 1, len(height)):
                max_found = max(min(height[j], h) * (j - idx), max_found)
        return max_found

if __name__ == '__main__':
    test_cases = [
        [1,8,6,2,5,4,8,3,7],
        [3, 9, 3, 4, 7, 2, 12, 6],
        [1,1],
        [2,3,4,5,18,17,6]
    ]
    correct_answers = [
        49,
        45,
        1,
        17
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.maxArea(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
