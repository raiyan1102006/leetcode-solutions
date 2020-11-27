# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Runtime: 604 ms, faster than 95.76% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.7 MB, less than 6.01% of Python3 online submissions for K Closest Points to Origin.


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            if len(heap)<K:
                heapq.heappush(heap,[-(x*x+y*y),[x,y]])
            else:
                heapq.heappushpop(heap,[-(x*x+y*y),[x,y]])
        return [pair for _,pair in heap]
        
#         hashDict = defaultdict(lambda:0)
#         for x,y in points:
#             hashDict[(x,y)] += x*x+y*y
#         return heapq.nsmallest(K,hashDict.keys(),key=hashDict.get)
        