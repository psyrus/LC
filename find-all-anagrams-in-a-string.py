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
        # Sliding window approach for anagrams
        # Need the character counts for the target (p)
        # Then get the character counts for a window in the string s
        output_idx = []

        if len(s) < len(p):
            return output_idx

        import collections
        target_len = len(p)
        target_counts = collections.Counter(p)
        window_counts = collections.Counter(s[0:target_len])

        # Only loop until the end of the string minus length of the target because the window is "target_len" characters long and we don't want to overrun the string length
        for i, c in enumerate(s[0:len(s) - target_len + 1]):
            check_window_str = s[i:i+target_len]
            # Check if this window has the same character counts as the target, if so, it is an anagram
            if target_counts == window_counts:
                output_idx.append(i)

            # Reduce the count of the value at i because on the next iteration the current i value will no longer be in the window
            window_counts[s[i]] -= 1

            if window_counts[s[i]] == 0:
                window_counts.pop(s[i])

            # Need to add the next item to the window, which is the current window right bound + 1
            if i + target_len < len(s):
                window_counts[s[i + target_len]] = window_counts.get(s[i + target_len], 0) + 1

        return output_idx

x = Solution()

print(x.findAnagrams("abab", "abaaaaa"))