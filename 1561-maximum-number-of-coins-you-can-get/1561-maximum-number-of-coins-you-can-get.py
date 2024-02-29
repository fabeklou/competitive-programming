class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        index = 1
        piles.sort(reverse=True)
        
        for _ in range(len(piles) // 3):
            coins += piles[index]
            index += 2

        return coins
