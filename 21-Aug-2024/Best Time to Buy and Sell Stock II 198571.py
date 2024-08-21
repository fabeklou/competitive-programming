# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyAt = -1
        profit = 0
        for index in range(len(prices)):
            if index == len(prices) - 1:
                # One last one for the road
                if buyAt != -1:
                    profit += prices[index] - prices[buyAt]
            else:
                # Time to buy
                if prices[index] < prices[index + 1] and buyAt == -1:
                    buyAt = index
                # Time to make profit
                elif prices[index] > prices[index + 1] and buyAt != -1:
                    profit += prices[index] - prices[buyAt]
                    buyAt = -1
        return profit
