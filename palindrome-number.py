# Given an integer x, return true if x is palindrome integer.
import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted = str(x)
        string_length = len(converted)
        left_pos = math.ceil(string_length / 2) - 1
        right_pos = left_pos + 1 if string_length % 2 == 0 else left_pos
        
        while left_pos >= 0 and right_pos < string_length:
            if converted[left_pos] != converted[right_pos]:
                return False
            left_pos -= 1
            right_pos += 1
        return True

if __name__ == '__main__':
    test_cases = [
        121,
        -121,
        10
    ]
    correct_answers = [
        True,
        False,
        False
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.isPalindrome(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
