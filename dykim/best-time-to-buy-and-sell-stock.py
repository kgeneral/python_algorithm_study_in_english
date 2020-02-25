# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# elapsed time : 28 min
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        curMin = prices[0]
        best = prices[1] - prices[0]
        for i in range(1, n):
            curMin = min(curMin, prices[i])
            best = max(prices[i] - curMin, best)
        
        return best
