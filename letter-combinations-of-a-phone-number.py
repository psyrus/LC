"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
2 = abc, 3 = def etc (1 has no mapping)
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        output = []
        # It feels like this could be a candidate for recursion?
        intermediate = []
        intermediate_idx = []
        for idx, d in enumerate(digits):
            intermediate.append(nums_to_letters[d])
            intermediate_idx.append(0)

        intermediate_idx_incr = len(intermediate_idx) - 1

        second_idx = len(intermediate_idx) - 1
        reached_end = False
        for primary_idx in range(len(digits)):
            while not intermediate_idx[0] > len(intermediate[0]) - 1:

                this_str = "".join([intermediate[i][intermediate_idx[i]]
                                    for i in range(primary_idx, len(intermediate))])
                output.append(this_str)

                intermediate_idx[-1] += 1

                if intermediate_idx[-1] < len(intermediate[-1]):
                    continue
                # Do any carry overs that need to happen
                for i in range(len(intermediate_idx) - 1, 0, -1):
                    if intermediate_idx[i] >= len(intermediate[i]):
                        if i == 1 and intermediate_idx[i - 1] == len(intermediate[i - 1]) - 1:
                            reached_end = True
                        intermediate_idx[i - 1] += 1
                        intermediate_idx[i] = 0

        return output


if __name__ == '__main__':
    test_cases = [
        "3343",
        "23",
        "",
        "2",
    ]
    correct_answers = [
        [],
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        [],
        ["a", "b", "c"],
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.letterCombinations(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
