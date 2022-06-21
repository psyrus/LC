# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List
class Solution:
    answers = []
    def recursiveGeneration(self, current_string, needed_open, needed_close):

        if needed_open > needed_close:
            return

        if not needed_open and not needed_close:
            self.answers.append(current_string)
            return
        
        if needed_open > 0:
            self.recursiveGeneration(current_string+"(", needed_open - 1, needed_close)
            
        if needed_close > 0:
            self.recursiveGeneration(current_string+")", needed_open, needed_close - 1)


    def generateParenthesis(self, n):
        # Recursively backtrack for open and closing characters
        # Use a class level variable to avoid the complexity of trying to combine the answers through the various calls
        self.answers = []
        opening = n
        closing = n

        self.recursiveGeneration("", opening, closing)
        return self.answers
        

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
