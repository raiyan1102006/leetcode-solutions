# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Runtime: 28 ms, faster than 83.26% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.3 MB, less than 41.19% of Python3 online submissions for Is Subsequence.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        s = list(s)
        t = list(t)

        while(1):
            last_elem_s = s.pop()
            while(1):
                last_elem_t = t.pop()
                if last_elem_s == last_elem_t:
                    if not len(s) and len(t)>=0:
                        return True
                    break
                if not len(t):
                    return False
            if not len(s):
                return False
                
        return True      
        