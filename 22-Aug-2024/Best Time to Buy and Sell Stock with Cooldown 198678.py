# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dp(index, operation):
            if len(prices) <= index:
                return 0
            if (index, operation) in cache:
                return cache[(index, operation)]
            # should we buy ?
            if operation:
                buy = dp(index + 1, False) - prices[index]
                cooldown = dp(index + 1, True)
                cache[(index, operation)] = max(buy, cooldown)
            # should we sell ?
            else:
                sell = dp(index + 2, True) + prices[index]
                cooldown = dp(index + 1, False)
                cache[(index, operation)] = max(sell, cooldown) 
            return cache[(index, operation)]

        return dp(0, True)  # BUY True, SELL False
