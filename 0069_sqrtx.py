# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Runtime: 28 ms, faster than 91.58% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.2 MB, less than 9.02% of Python3 online submissions for Sqrt(x).


class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        left = 2
        right = x//2
        while (left<=right):
            mid = left+(right-left)//2
            sq = mid*mid
            if (sq)>x:
                right = mid -1
            elif (sq)<x:
                left = mid +1
            else:
                return mid

        return right
        