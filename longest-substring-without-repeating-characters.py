# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def getLongestSequenceFromIndex(self, start_idx: int, s: str) -> int:
        seq_length = 0
        seen = []
        idx = start_idx
        while idx < len(s):
            if s[idx] in seen:
                break
            seen.append(s[idx])
            seq_length += 1
            idx += 1
        return seq_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force approach
        longest_string_found = 0
        for str_start in range(0, len(s)):
            this_longest_sequence = self.getLongestSequenceFromIndex(str_start, s)
            if this_longest_sequence > longest_string_found:
                longest_string_found = this_longest_sequence
        return longest_string_found

if __name__ == '__main__':
    x = Solution()
    input_string = " "
    print(x.lengthOfLongestSubstring(input_string))