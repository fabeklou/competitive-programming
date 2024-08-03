# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                coins[5] += 1
            elif bill == 10:
                coins[10] += 1
                coins[5] -= 1
            else:
                if coins[10]:
                    coins[10] -= 1
                    coins[5] -= 1
                else:
                    coins[5] -= 3

            if coins[5] < 0 or coins[10] < 0: return False
        return True