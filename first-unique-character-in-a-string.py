"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeating_idx = None
        char_idx = {}
        for i, c in enumerate(s):
            char_idx[c] = char_idx.get(c, []) + [i]


        for c in char_idx:
            if len(char_idx[c]) > 1:
                continue
            this_min = min(char_idx[c])
            non_repeating_idx = this_min if None == non_repeating_idx else min(non_repeating_idx, this_min)
        return -1 if None == non_repeating_idx else non_repeating_idx