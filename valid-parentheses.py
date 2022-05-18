"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # Classic problem - Use a stack to determine the opening and closing characters match
        # Push to the stack on an open, pop from the stack on a close
        # Use a hashtable to keep the association together

        stack = []
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                check_char = stack.pop() if len(stack) > 0 else None
                if not check_char or bracket_map[c] != check_char:
                    return False

        # There are edge cases people forget about which is if it is all opening brackets so we are left with an unpopped stack
        return len(stack) == 0