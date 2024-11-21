# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        f = [0, *flowerbed, 0]
        for index in range(1, len(f) - 1):
            if f[index] == f[index-1] == f[index+1] == 0:
                f[index] = 1
                n -= 1
                if n == 0: return True
        return False
