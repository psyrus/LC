from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        lowest_length = min([len(i) for i in strs])
        if len(strs) == 1:
            return strs[0]

        common_final_idx = -1
        for i in range(0, lowest_length):
            check_char = strs[0][i]
            all_same = True
            for s in strs[1:]:
                if s[i] != check_char:
                    all_same = False
                    break
            if all_same:
                common_final_idx = i
            else:
                break


        return strs[0][:common_final_idx + 1]
        
if __name__ == '__main__':
    test_cases = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["ab", "a"],
    ]
    correct_answers = [
        "fl",
        "",
        "a"
    ]
    x = Solution()
    for i, t in enumerate(test_cases):
        my_answer = x.longestCommonPrefix(t)
        print(
            f"{'Correct' if my_answer == correct_answers[i] else 'Wrong'} : {my_answer} ({correct_answers[i]})"
        )
