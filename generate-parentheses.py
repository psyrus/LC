# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List
class Solution:
    def generateRecursive(self, n:int, current_list: List[str]) -> List[str]:
        if n > 1:
            recursive_output = self.generateRecursive(n - 1, current_list)
            for i in range(len(recursive_output)):
                v = recursive_output[i]
                recursive_output[i] = (f"{v}()")
                recursive_output.append(f"(){v}")
                recursive_output.append(f"({v})")
            return recursive_output

        return ["()"]

        return recursive_output
    def generateParenthesis(self, n: int) -> List[str]:
        # Pattern 1: fully embedded
        # Pattern 2: fully side by side
        # Pattern 3: all side by side except last
        # Pattern 4: Mixed of the above pieces

        output = self.generateRecursive(n, [])
        # This definitely feels like a recursive item
        return list(set(output))

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
# Missing from 4: '(())(())'
# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
# ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']