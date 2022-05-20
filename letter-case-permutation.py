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
        str_len = len(s)
        def helper(idx, substring):
            if idx == str_len:
                return [substring]

            results = []

            char = s[idx]
            if char.isalpha():
                if char.islower():
                    results += helper(idx+1, substring+char.upper())
                else:
                    results += helper(idx+1, substring+char.lower())
            results += helper(idx+1,substring+char)

            return results

        return helper(0, '')

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