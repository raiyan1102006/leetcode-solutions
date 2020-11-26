# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# Runtime: 24 ms, faster than 95.42% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.2 MB, less than 49.80% of Python3 online submissions for Decode Ways.


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1 
        dp[1] = 1 if s[0]!= '0' else 0 #how many ways to get to the first digit
        
        for i in range(2,len(dp)):
            if s[i-1] != '0':
                dp[i]+=dp[i-1]
            
            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <=26:
                dp[i] += dp[i-2]
                
        return(dp[-1])
        