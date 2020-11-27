# 836. Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/
# Runtime: 24 ms, faster than 93.05% of Python3 online submissions for Rectangle Overlap.
# Memory Usage: 14.3 MB, less than 6.50% of Python3 online submissions for Rectangle Overlap.


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0]==rec1[2] or rec1[1]==rec1[3] or rec2[0]==rec2[2] or rec2[1]==rec2[3]: return False
        
        return not (rec2[2]<=rec1[0] or rec1[2]<= rec2[0] or 
                   rec2[3]<=rec1[1] or rec1[3]<= rec2[1])