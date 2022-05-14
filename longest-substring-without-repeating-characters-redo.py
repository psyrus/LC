"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_start = 0
        s_end = 0
        longest = 0
        seen_chars = {}
        while s_end < len(s):
            if s[s_end] in seen_chars and s_start <= seen_chars[s[s_end]]:
                s_start = seen_chars[s[s_end]] + 1
            else:
                longest = max(longest, s_end - s_start + 1)

            seen_chars[s[s_end]] = s_end
            s_end += 1

        return longest