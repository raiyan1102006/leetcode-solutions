# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Runtime: 44 ms, faster than 89.81% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 93.92% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hashTable:
                hashTable[nums[i]] = i
            else:
                return [hashTable[complement], i]