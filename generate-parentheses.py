# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List
class Solution:
    def generateParenthesis(self, n):
        
        # Recursively backtrack for open and closing characters

if __name__ == '__main__':
    test_cases = [
        4,
        3,
        2,
        1,
    ]
    correct_answers = [
        ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"],
        ["((()))","(()())","(())()","()(())","()()()"],
        ["()()", "(())"],
        ["()"],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.generateParenthesis(t)
        print(
            f"{'Correct' if sorted(my_answer) == sorted(correct_answers[i]) else 'Wrong'} : {sorted(my_answer)} \033[1;32m ({sorted(correct_answers[i])})\u001b[37m"
        )
