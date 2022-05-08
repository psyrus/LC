"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip(" ")
        for i in range(len(s)):
            if s[len(s) - i - 1] == " ":
                break

            length += 1

        return length

if __name__ == '__main__':
    test_cases = [
        "a",
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
    ]
    correct_answers = [
        1,
        5,
        4,
        6,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.lengthOfLastWord(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
