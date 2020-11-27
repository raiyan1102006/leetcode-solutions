# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
# Runtime: 652 ms, faster than 75.19% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 70.2 MB, less than 30.19% of Python3 online submissions for Time Based Key-Value Store.



class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.HashTable = defaultdict(lambda:[])

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.HashTable[key], (-timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        for t,v in self.HashTable[key]:
            if -t<=timestamp: #we have to take -t because -timestamp was pushed to the heap act like maxheap. Taking the negative of t here restores t to the real value it has. 
                return v
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)