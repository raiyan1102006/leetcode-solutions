# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 96 ms, faster than 77.79% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.8 MB, less than 12.26% of Python3 online submissions for Top K Frequent Elements.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        tally = defaultdict(lambda:0)
        for n in nums:
            tally[n]+=1
        
        # sorted_ = sorted(tally, key = tally.get, reverse=True)
        # return(sorted_[:k])
        return heapq.nlargest(k,tally.keys(), key=tally.get)
        
        