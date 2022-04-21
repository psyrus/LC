class Solution:
    # This is my terrible first approach
    def isPalindrome(self, substr: list[str]) -> bool:
        # While i is less than half way (len // 2), check if the + and - index match as characters
        if len(substr) == len(set(substr)):
            return True
        for i in range(0, len(substr) // 2):
            left_char = substr[i]
            right_char = substr[len(substr) - i - 1]
            if left_char != right_char:
                return False
        return True
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) == len(set(s)):
            return s[0]
        char_pos = {}
        for i, v in enumerate(s):
            if v not in char_pos:
                char_pos[v] = []
            char_pos[v].append(i)

        longest_palindrome = ''
        for c in char_pos.keys():
            left_itr = 0
            while left_itr < len(char_pos[c]) - 1:
                right_itr = len(char_pos[c]) - 1
                if right_itr - left_itr <= len(longest_palindrome):
                    break
                while right_itr > left_itr:
                    left_index = char_pos[c][left_itr]
                    right_index = char_pos[c][right_itr]
                    if right_index - left_index <= len(longest_palindrome):
                        break
                    palindrome_candidate = s[left_index:right_index + 1]
                    if self.isPalindrome(palindrome_candidate):
                        longest_palindrome = longest_palindrome if len(longest_palindrome) > len(palindrome_candidate) else palindrome_candidate
                        break
                    right_itr -= 1
                left_itr += 1
            
        return longest_palindrome or s[0]

class Solution:
    # This is based on a discussion - I only made it easier to understand. Will need to try this one from scratch
    def palindrome_helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        retstr = s[l+1:r]
        return retstr
                
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        for i in range(len(s)):
            odd_palindrome_check = self.palindrome_helper(s, i, i)
            even_palindrome_check = self.palindrome_helper(s, i, i + 1)

            if len(even_palindrome_check) > len(longest_palindrome):
                longest_palindrome = even_palindrome_check
            if len(odd_palindrome_check) > len(longest_palindrome):
                longest_palindrome = odd_palindrome_check

        return longest_palindrome

if __name__ == '__main__':
    test_cases = [
        "aacabdkacaa",
        "a",
        "ac",
        "babad",
        # "cbbd",
        # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ]
    x = Solution()
    for t in test_cases:
        print(x.longestPalindrome(t))