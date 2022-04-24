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

class NoStringSolution:
    def getNumAtPos(self, number: int, pos: int) -> int:
        return ((number % (10 ** pos)) // (10 ** (pos - 1)))

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        tens_power_itr = 0
        while (10 ** tens_power_itr) <= x:
            tens_power_itr += 1

        number_length = tens_power_itr
        # To get the third digit, num % (10 ** 3) // (10 ** 2)
        # To get the nth digit, num  % (10 ** n) // (10 ** n-1)

        left_pos = math.ceil(number_length / 2) - 1
        right_pos = left_pos + 1 if number_length % 2 == 0 else left_pos

        while left_pos >= 0 and right_pos < number_length:
            # Need to convert the index to the "position" in the number based on the digits counting up from the smallest part of the number (right side)
            l = self.getNumAtPos(x, number_length - left_pos)
            r = self.getNumAtPos(x, number_length - right_pos)
            if l != r:
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


    y = NoStringSolution()
    for i, t in enumerate(test_cases):
        my_answer = y.isPalindrome(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )