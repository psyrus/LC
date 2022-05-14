"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Imagine I can't use the count() feature in python

        s1_char_counts = {}
        for c in s1:
            if c not in s1_char_counts:
                s1_char_counts[c] = 0

            s1_char_counts[c] += 1

        for i, c in enumerate(s2):
            if i > len(s2) - len(s1):
                return False
            if c in s1_char_counts:
                # Start a sliding window to check if all the character counts match
                char_counts = {}
                invalid_char_found = False
                for j in range(i, i + len(s1)):
                    this_c = s2[j]
                    if this_c not in s1_char_counts:
                        invalid_char_found = True
                        break
                    if this_c not in char_counts:
                        char_counts[this_c] = 0

                    char_counts[this_c] += 1

                if not invalid_char_found:
                    all_valid = True
                    for check_c in s1_char_counts:
                        if check_c not in char_counts or s1_char_counts[check_c] != char_counts[check_c]:
                            all_valid = False
                            break

                    if all_valid:
                        return True
        return False

x = Solution()
print(x.checkInclusion("adc", "dcda"))