"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output_negative = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0

        if output_negative:
            for i in range(-1, dividend, -1):
                total = 0
                for j in range(1, divisor + 1):
                    total += i
                if total > dividend:
                    return i - 1
        else:
            for i in range(1, dividend + 1):
                total = 0
                for j in range(1, divisor + 1):
                    total += i
                if total > dividend:
                    return i - 1
        raise ValueError("This is not good")

if __name__ == '__main__':
    test_cases = [
        (10, 3),
        (7, 3),
        (-7, 3),
    ]
    correct_answers = [
        3,
        2,
        -2,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.divide(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
