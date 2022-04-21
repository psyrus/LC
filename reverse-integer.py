class Solution:
    def check_legit(self, s: str, compare_s: str) -> bool:
        if len(s) < len(compare_s):
            return True
        for idx, val in enumerate(s):
            if val == compare_s[idx]:
                continue
            elif int(val) > int(compare_s[idx]):
                return False
            elif int(val) < int(compare_s[idx]):
                return True
        return True

    def reverse(self, x: int) -> int:
        compare_str = str(2**31 - 1) if x > 0 else str(-2**31)
        reversed_int = (str(x))[::-1]
        # reversed_int = reversed_int.lstrip("0")
        reversed_int = reversed_int.rstrip("-")
        if x < 0:
            reversed_int = "-" + reversed_int

        # Check if the value is too large or too small
        return int(reversed_int) if self.check_legit(reversed_int, compare_str) else 0

if __name__ == '__main__':
    test_cases = [
        123,
        -123,
        120
    ]
    correct_answers = [
        321,
        -321,
        21
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.reverse(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
