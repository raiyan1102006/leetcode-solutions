# 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/
# Runtime: 232 ms, faster than 84.15% of Python3 online submissions for Design Underground System.
# Memory Usage: 23.8 MB, less than 53.10% of Python3 online submissions for Design Underground System.


class UndergroundSystem:

    def __init__(self):
        self.completedDict = defaultdict(lambda:[])
        self.ongoing={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing[id]=(stationName,t)
 
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        entryStationName, entryTime = self.ongoing.pop(id)
        self.completedDict[(entryStationName,stationName)].append(t-entryTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.completedDict[(startStation,endStation)])/len(self.completedDict[(startStation,endStation)])
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)