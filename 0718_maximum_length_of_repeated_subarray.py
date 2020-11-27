# 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Runtime: 2588 ms, faster than 87.72% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.4 MB, less than 38.99% of Python3 online submissions for Maximum Length of Repeated Subarray.


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return(max(max(row) for row in memo))