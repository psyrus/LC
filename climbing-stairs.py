"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = 0
        if n == 1:
            return 1

        step1 = 1
        step2 = 2

        for i in range(2, n):
            tmp = step2
            step2 = step1 + step2
            step1 = tmp

        return step2

if __name__ == '__main__':
    test_cases = [
        2,
        3,
    ]
    correct_answers = [
        2,
        3,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.lengthOfLastWord(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
