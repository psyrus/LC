"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
        return -1