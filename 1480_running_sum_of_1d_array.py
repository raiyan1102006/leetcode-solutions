# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Runtime: 32 ms, faster than 94.60% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.6 MB, less than 11.39% of Python3 online submissions for Running Sum of 1d Array.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for i in range(1,len(nums)):
            output.append(output[-1]+nums[i])
        return output