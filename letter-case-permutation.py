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
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        letter_positions_to_permute = []
        for i, c in enumerate(s):
            if c.isdigit():
                continue
            letter_positions_to_permute.append(i)

        output = []
        def caseHelper(permute_char_list:List[str], positions:List[int], existing_combos:List[List[str]]):
            if not positions:
                return existing_combos

            this_iteration = []
            for i, v in enumerate(positions):
                items = caseHelper(permute_char_list, positions[i+1:], existing_combos + [permute_char_list])
                updated = permute_char_list.copy()
                updated[v] = updated[v].upper()
                items += caseHelper(permute_char_list, positions[i+1:], existing_combos + [updated])
                for c in items:
                    print(c)
            return this_iteration


        output = caseHelper(list(s), letter_positions_to_permute, [])
        return output

x = Solution()
print(x.letterCasePermutation("a1b2"))
print(x.letterCasePermutation("3z4"))