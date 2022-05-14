"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Imagine I can't use the count() feature in python

        # s1_char_counts = {}
        # for c in s1:
        #     if c not in s1_char_counts:
        #         s1_char_counts[c] = 0
        #     s1_char_counts[c] += 1
        ### The above can be simplfied to one line using collections
        import collections
        s1_len = len(s1)

        # Initialize the character counts for s1, and for a window in s2 that is the same size as s1 (0 to s1_len)
        s1_char_counts = collections.Counter(s1)
        s2_window_counts = collections.Counter(s2[0:s1_len])

        # Do a quick check to see if we can return early without looping at all
        if s1_char_counts == s2_window_counts:
            return True

        # Loop the left side of the window until the end of s2 minus len(s1) because the right side of the window is i + len(s1)
        # Note: Even though the loop starts at 0, the first iteration is already checking for the window in indeces: 1 to 1 + len(s1) which is why the quick return check was done above
        for i in range(len(s2) - s1_len):
            window_left_char = s2[i]
            window_right_char = s2[i + s1_len]

            # Decrement the counter of the current character (i) in s2, and if the count would be 0, then remove it entirely from the count
            if s2_window_counts[window_left_char] == 1:
                s2_window_counts.pop(window_left_char)
            elif s2_window_counts[window_left_char] > 1:
                s2_window_counts[window_left_char] -= 1

            # Add the counter of the character at the right of the window
            if window_right_char not in s2_window_counts:
                s2_window_counts[window_right_char] = 0

            s2_window_counts[window_right_char] += 1

            # Finally - Check if the counts of all characters in the window (i to i + s1_len) match those in s1, which means they are anagrams
            if s1_char_counts == s2_window_counts:
                return True

        # If we never found a window that matched s1 character counts, return False by default
        return False

x = Solution()
print(x.checkInclusion("adc", "dcda"))