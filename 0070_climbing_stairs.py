# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Runtime: 24 ms, faster than 90.64% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14 MB, less than 75.21% of Python3 online submissions for Climbing Stairs.


class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        dp = [1,2]+[0]*(n-2)

        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[-1]        