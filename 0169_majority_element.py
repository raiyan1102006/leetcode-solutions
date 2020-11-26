# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Runtime: 164 ms, faster than 53.69% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 6.55% of Python3 online submissions for Majority Element.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = defaultdict(lambda:0)
        for n in nums:
            hashMap[n]+=1

        k = list(hashMap.keys())
        v = list(hashMap.values())
        return k[v.index(max(v))]
