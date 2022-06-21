"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [set() for i in range(n+1)]
        dp[0] = set([""])

        for this_iteration in range(1, n + 1):
            for prev_iterations_iterator in range(this_iteration):
                left = dp[prev_iterations_iterator]
                right = dp[this_iteration - prev_iterations_iterator - 1]
                for l_item in left:
                    for r_item in right:
                        dp[this_iteration].add("(" + l_item + ")" + r_item)

        return dp[n]

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

# [ '()(())()', '()(())()', ]
# [ '(())(())',  '()(())()', ]