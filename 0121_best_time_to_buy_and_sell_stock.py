# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 52 ms, faster than 96.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.1 MB, less than 10.07% of Python3 online submissions for Best Time to Buy and Sell Stock.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        maxprofit = 0
        minprice = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minprice:
                minprice = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i]-minprice)
        return(maxprofit)