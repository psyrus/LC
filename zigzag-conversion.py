class Solution:
    # 1 < len(s) < 1000
    # 1 < numRows < 1000
    # s contains [A-z,.]
    # ZigZag means go down on current col, then +x +y until at the top again, repeat
    def convert(self, s: str, numRows: int) -> str:
        # Edge case of only one row
        if numRows == 1:
            return s

        iterator_val = 0 # swaps between + and -
        levels = [[] for i in range(0, numRows)]
        level_tracker = 0
        for c in s:
            levels[level_tracker].append(c)

            # Handle iterator flip
            if level_tracker == numRows - 1:
                iterator_val = -1
            elif level_tracker == 0:
                iterator_val = 1
            
            level_tracker += iterator_val

        # Once the levels are all populated, combine them to output as a string
        combined_arrays = []
        for v in levels:
            combined_arrays += v
        return "".join(combined_arrays)


if __name__ == '__main__':
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
        ("ABC", 1)
    ]
    correct_answers = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
        "ABC"
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.convert(t[0], t[1])
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer}"
        )
