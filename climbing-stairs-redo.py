"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Input: n = 4
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 2 steps + 1 step
3. 2 steps + 1 step + 1 step
4. 1 step + 1 step + 2 steps
5. 2 steps + 2 steps

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Somehow you just understand that this is a fibbonacci sequence

        # Implemented recursively it will be count(n) = count(n-1) + count(n-2) .. + count(0)
        step_counts = {}
        def getStepCount(num_steps_remaining: int):
            # Base case: One step? Zero steps?
            if num_steps_remaining < 3:
                return num_steps_remaining

            # Memoization cheat code:
            if num_steps_remaining in step_counts:
                return step_counts[num_steps_remaining]

            # Recursive relation: current_remaining = current_remaining - 1 + current_remaining - 2
            this_steps = getStepCount(num_steps_remaining - 1) + getStepCount(num_steps_remaining - 2)
            step_counts[num_steps_remaining] = this_steps
            return this_steps

        return getStepCount(n)

    def climbStairsIterative(self, n: int) -> int:
        step_counts = {}

        for v in range(n + 1):
            if v <= 2:
                step_counts[v] = v
            else:
                step_counts[v] = step_counts[v-1] + step_counts[v-2]

        return step_counts[n]

x = Solution()
print(x.climbStairsIterative(4))
print(x.climbStairsIterative(3))
print(x.climbStairsIterative(2))
print(x.climbStairsIterative(1))