# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/
# Runtime: 720 ms, faster than 74.46% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.9 MB, less than 12.87% of Python3 online submissions for Find the Town Judge.


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1: return 1
        in_degree = defaultdict(lambda:0)
        out_degree = defaultdict(lambda:0)
        
        for a,b in trust:
            in_degree[b]+=1
            out_degree[a]+=1
        for key,val in in_degree.items():
            if val==N-1 and not out_degree[key]:
                return key

        return -1