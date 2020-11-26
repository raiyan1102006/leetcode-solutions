# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# Runtime: 24 ms, faster than 94.71% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.3 MB, less than 17.05% of Python3 online submissions for Unique Paths.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n-1) + [1]]*(m-1)
        dp.append([1]*n)
        
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                dp[row][col] = dp[row+1][col]+dp[row][col+1]
                
        return(dp[0][0])