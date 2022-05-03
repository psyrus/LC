class Solution:
    def matches(self, match_target, character):
        return character in [match_target, '.']

    def isMatch(self, s: str, p: str) -> bool:
        match_char = ''
        reg_itr = 0

        # Loop through main string
        # Check if the char matches exactly or the wildcard char
        # if the "check" character is a *, take the match char as the one before the *
        # When a non-match is found, move to the next matching character

        for main_itr, c in enumerate(s):
            if p[reg_itr] == '*':
                reg_itr -= 1
            match_char = p[reg_itr]

            if not self.matches(match_char, c):
                if reg_itr == len(p) - 1:
                    return False
                

        return True

if __name__ == '__main__':
    test_cases = [
        ("aa", "a"),
        ("aa", "a*"),
        ("ab", ".*"),
    ]
    correct_answers = [
        False,
        True,
        True,
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.isMatch(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
