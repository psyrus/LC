"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # First get the char counts of the second string

        char_counts_p = {}
        len_s = len(s)
        len_p = len(p)
        for v in p:
            char_counts_p[v] = char_counts_p.get(v, 0) + 1

        upper_bound = len_s - len_p + 1
        # need to initalize because we're starting from 0 index
        char_counts_s = {}
        for v in s[:len_p]:
            char_counts_s[v] = char_counts_s.get(v, 0) + 1

        output = []
        for i in range(upper_bound):
            if all([char_counts_s.get(v, 0) == count for v, count in char_counts_p.items()]):
                output.append(i)

            # Have to add this stupid check because otherwise it will go out of bounds when checking the last item
            # Theoretically we could shift everything offset by one to the left and include the add/remove at the start to ensure it doesn't exceed bounds..
            if i < upper_bound - 1:
                char_counts_s[s[i]] = char_counts_s.get(s[i], 0) - 1
                char_counts_s[s[i+len_p]] = char_counts_s.get(s[i+len_p], 0) + 1

        return output

x = Solution()
print(x.findAnagrams("abab", "ab"))