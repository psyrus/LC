# Given a string s, find the length of the longest substring without repeating characters.
from turtle import right


class SolutionBruteForce:
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

class Solution:
    def getNextLeftIteration(self, start_left_idx: int, input_string: str, duplicated_char: str):
        leftmost_possible = (input_string[start_left_idx:]).index(duplicated_char) + 1 + start_left_idx
        # while leftmost_possible < len(input_string) - 1 and input_string[leftmost_possible + 1] == duplicated_char:
        #     leftmost_possible += 1
        return leftmost_possible

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Efficient approach
        longest_string_found = 0
        left_iter = right_iter = 0
        

        while left_iter < len(s):
            seen = [] # Don't forget to pop duplicate out as moving left iter
            right_iter = max(left_iter, right_iter)
            while True:
                if right_iter >= len(s):
                    # Reached the end of the string
                    return max(len(seen), longest_string_found)
                if s[right_iter] in seen:
                    # Found a duplicate so we need to save the longest string val and reorient the left side
                    longest_string_found = max(len(seen), longest_string_found)
                    left_iter = self.getNextLeftIteration(left_iter, s, s[right_iter])
                    break
                seen.append(s[right_iter])
                right_iter += 1
        return longest_string_found

if __name__ == '__main__':
    x = Solution()
    input_string = "dvdf"
    print(x.lengthOfLongestSubstring(input_string))