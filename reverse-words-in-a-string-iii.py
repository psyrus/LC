"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""
class Solution:
    def reverseString(self, s:str) -> str:

        output_arr = [c for c in s]
        for i in range(len(output_arr) // 2):
            r = len(output_arr) - 1 - i
            output_arr[i] = s[r]
            output_arr[r] = s[i]
        return "".join(output_arr)

    def reverseWords(self, s: str) -> str:
        reversed_string_list = []
        words = s.split(" ")

        for w in words:
            reversed_string_list.append(self.reverseString(w))

        return " ".join(reversed_string_list)