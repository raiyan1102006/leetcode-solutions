# 277. Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/
# Runtime: 1524 ms, faster than 93.28% of Python3 online submissions for Find the Celebrity.
# Memory Usage: 14.4 MB, less than 19.18% of Python3 online submissions for Find the Celebrity.


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n       
        celeb_candidate = 0
        for i in range(1,n):
            if knows(celeb_candidate,i):
                celeb_candidate= i
        if self.isCelebrity(celeb_candidate): return celeb_candidate
        return -1

    def isCelebrity(self, i):
        for j in range(self.n):
            if i==j: continue
            if knows(i,j) or not knows(j,i):
                return False
        return True
        
