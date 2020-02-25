# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# elapsed time : 28 min
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        n = len(prices)
        dp = {}
        curMin = prices[0]
        best = prices[1] - prices[0]
        for i in range(1, n):
            print(prices[i], curMin, best)
            curMin = min(curMin, prices[i])
            best = max(prices[i] - curMin, best)
        
        return best
