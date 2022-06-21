"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Starting from the back of both strings
        # Keep track of the "skip" (#) chars
        # When there are no skip chars for either, there should be equivalence in the chars between s1 and s2

        s_idx = len(s)
        t_idx = len(t)
        s_skip = 0
        t_skip = 0

        # Ensure we loop while either string still has active characters available
        while s_idx >= 0 or t_idx >= 0:
            s_idx -= 1
            t_idx -= 1

            while s_idx >= 0 and (s[s_idx] == "#" or s_skip > 0):
                if s[s_idx] == "#":
                    s_skip += 1
                else:
                    s_skip -= 1
                s_idx -= 1

            while t_idx >= 0 and (t[t_idx] == "#" or t_skip > 0):
                if t[t_idx] == "#":
                    t_skip += 1
                else:
                    t_skip -= 1
                t_idx -= 1

            # If either one has exhausted all characters, but the other one has not, that's a definite failure
            if (s_idx < 0 and t_idx >= 0) or (s_idx >= 0 and t_idx < 0):
                return False

            # Assuming both still have active characters, check if the character at each respective index is equivalent or not. If not, it's a failed string
            if (t_idx >= 0 and s_idx >= 0) and t[t_idx] != s[s_idx]:
                return False
        return True


x = Solution()
print(x.backspaceCompare("ab#cc#", "ad#c"))
print(x.backspaceCompare("a##c", "#a#c"))
print(x.backspaceCompare("nzp#o#g", "b#nzp#o#g"))
print(x.backspaceCompare("a#c#c", "##########"))
print(x.backspaceCompare("ab#c", "ad#c"))
print(x.backspaceCompare("ab##", "c#d#"))
print(x.backspaceCompare("a#c", "b"))
