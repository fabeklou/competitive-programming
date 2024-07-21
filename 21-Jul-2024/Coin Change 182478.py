# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dq = deque([(0, 0)])  # choices, state 
        visited = set([0])
        min_coins = float('+inf')

        while dq:
            choices, state = dq.popleft()

            if state == amount:
                return choices

            for coin in coins:
                if state + coin not in visited and state + coin <= amount:
                    dq.append((choices + 1, coin + state))
                    visited.add(state + coin)

        return min_coins if min_coins != float('+inf') else -1
        