# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
# Runtime: 24 ms, faster than 92.35% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.2 MB, less than 30.51% of Python3 online submissions for Fibonacci Number.


class Solution:
    def fib(self, N: int) -> int:
        if N<=1:
            return N
        dp = [1,1]
        for i in range(2,N):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]

        