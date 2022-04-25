class Solution:
    def intToRoman(self, num: int) -> str:
        rules = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M"),
        ]
        # Can either do it via string (position) or int value (% and //)
        # Try int first
        output = ""
        for v, c in rules[::-1]:
            # Get how many of this number remain
            contained = num // v
            for i in range(contained):
                output += c
            remaining = num - (v * contained)
            num = remaining
        return output


if __name__ == '__main__':
    test_cases = [
        3,
        58,
        1994,
        9,
    ]
    correct_answers = [
        "III",
        "LVIII",
        "MCMXCIV",
        "IX",
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.intToRoman(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
