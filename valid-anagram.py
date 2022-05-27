"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Note I will not use built in "count" to ensure I could implement this in a different language if necessary

        if len(s) != len(t):
            return False

        s_counts = {}
        for c in s:
            s_counts[c] = s_counts.get(c, 0) + 1

        t_counts = {}
        for c in t:
            # Quick check to break early if any chars are different
            if c not in s_counts:
                return False
            t_counts[c] = t_counts.get(c, 0) + 1

        for c in s_counts:
            if s_counts[c] != t_counts[c]:
                return False

        return True