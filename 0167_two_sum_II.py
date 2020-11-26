# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Runtime: 44 ms, faster than 99.96% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.7 MB, less than 8.36% of Python3 online submissions for Two Sum II - Input array is sorted.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashDict = {}
        for i in range(len(numbers)):
            compl = target - numbers[i]
            if compl not in hashDict:
                hashDict[numbers[i]] = i
            else: return [hashDict[compl]+1,i+1]