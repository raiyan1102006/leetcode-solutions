# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/
# Runtime: 56 ms, faster than 81.40% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.4 MB, less than 12.92% of Python3 online submissions for Shuffle the Array.


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i,j in zip(range(n),range(n,len(nums))):
            output.extend([nums[i],nums[j]])
        return output