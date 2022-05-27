"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 
Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""
import enum
from typing import List
class Solution:
    def letterCasePermutationRecursive(self, s: str) -> List[str]:
        res = []
        s = s.lower()
        def combineChars(original_string: str, evaluate_idx: int, current_substring: List[str]):
            if len(current_substring) == len(original_string):
                res.append("".join(current_substring))
                return

            current_substring.append(original_string[evaluate_idx])
            if not original_string[evaluate_idx].isdigit():
                combineChars(original_string, evaluate_idx+1, current_substring)
                current_substring[-1] = current_substring[-1].upper()
                combineChars(original_string, evaluate_idx+1, current_substring)
            else:
                combineChars(original_string, evaluate_idx+1, current_substring)

            current_substring.pop()

        combineChars(s, 0, [])
        return res

    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s.lower())
        letter_positions_to_permute = []
        for i, c in enumerate(s):
            if c.isdigit():
                continue
            letter_positions_to_permute.append(i)

        output = [s]
        for pos in letter_positions_to_permute:
            # append uppercase version of the current char mutation for each item already in output
            for i in range(len(output)):
                upper = output[i].copy()
                upper[pos] = upper[pos].upper()
                output.append(upper)
        return ["".join(i) for i in output]

x = Solution()
print(x.letterCasePermutationRecursive("a1b2"))
print(x.letterCasePermutationRecursive("3z4"))
print(x.letterCasePermutationRecursive("28djkZd3"))