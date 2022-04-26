class Solution:
    def romanToInt(self, s: str) -> int:
        rules = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        special_rules = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        # Can either do it via string (position) or int value (% and //)
        # Try int first
        output = 0
        i = 0
        while i < len(s):
            look_ahead = s[i:i + 2] if i < len(s) - 1 else ""
            if look_ahead in special_rules.keys():
                output += special_rules[look_ahead]
                i += 2
            else:
                output += rules[s[i]]
                i += 1
        return output


if __name__ == '__main__':
    correct_answers = [
        3,
        58,
        1994,
        9,
    ]
    test_cases = [
        "III",
        "LVIII",
        "MCMXCIV",
        "IX",
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.romanToInt(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
