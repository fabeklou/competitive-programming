class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float('+inf'), float('-inf')
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            if (price - buy) > profit:
                sell = price
                profit = max(profit, sell - buy)
        return profit
