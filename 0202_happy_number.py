# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Runtime: 24 ms, faster than 97.95% of Python3 online submissions for Happy Number.
# Memory Usage: 14.1 MB, less than 77.91% of Python3 online submissions for Happy Number.


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while (1):
            sum_sq = 0
            while(n):
                n,vagshesh = divmod(n,10)
                sum_sq+=vagshesh*vagshesh
            
            if sum_sq ==1:
                return True
            elif sum_sq in visited:
                return False
            else:
                visited.add(sum_sq)
                n = sum_sq