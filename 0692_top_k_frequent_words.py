# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/
# Runtime: 48 ms, faster than 94.74% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14.2 MB, less than 36.71% of Python3 online submissions for Top K Frequent Words.


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hashDict = defaultdict(lambda:0)
        for w in words:
            hashDict[w]+=1
        
        sorted_ = sorted([(-count,word) for word,count in hashDict.items()])
        return([j[1] for j in sorted_[:k]])
    
#         heaplist =[(-count,word) for word,count in hashDict.items()]
#         heapq.heapify(heaplist)
#         return [heapq.heappop(heaplist)[1] for _ in range(k)]