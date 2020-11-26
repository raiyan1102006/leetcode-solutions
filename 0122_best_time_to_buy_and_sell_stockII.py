# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Runtime: 60 ms, faster than 60.08% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 14.9 MB, less than 75.28% of Python3 online submissions for Best Time to Buy and Sell Stock II.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                profit+= (prices[i] - prices[i-1])
        return(profit)