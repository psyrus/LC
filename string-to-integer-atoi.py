class Solution:
    # ignore leading whitespace
    # first non whitespace char may be + or -
    # all characters in 0-9 acccepted
    # first non numeric character triggers the rest of the string to be ignored
    # ensure any integers that go outside the 32bit bounds are just returned as those max/min values
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if len(s) == 0:
            return 0
        sign_chgr = 1
        if s[0] == "+":
            s  = s[1:]
        elif s[0] == "-":
            sign_chgr = -1
            s  = s[1:]

        endIndex = len(s)
        compare_arr = [str(i) for i in range(10)]
        for idx, val in enumerate(s):
            if val not in compare_arr:
                endIndex = idx
                break
        result = int(s[0:endIndex]) if endIndex > 0 else 0
        result = result * sign_chgr
        # Bind to min\max values
        result = max(result, -2**31) if result < 0 else min(result, 2**31 - 1)
        return result


if __name__ == '__main__':
    test_cases = [
        
"+-12",
"-91283472332",
       "42",
       "   -42",
       "4193 with words",
       "words and 987"
    ]
    correct_answers = [
        0,
        -2147483648,
        42,
        -42,
        4193,
        0
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.myAtoi(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
