# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pds = [(p, d) for p, d in zip(profit, difficulty)]
        pds.sort(reverse=True)
        max_profit = ptr = 0
        for w in sorted(worker, reverse=True):
            while ptr < len(profit) and pds[ptr][1] > w:
                ptr += 1
            if ptr >= len(profit):
                break
            max_profit += pds[ptr][0]
        return max_profit
