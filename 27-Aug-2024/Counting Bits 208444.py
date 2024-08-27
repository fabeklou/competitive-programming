# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            while num:
                if num < len(res):
                    count += res[num]
                    break
                if num % 2:
                    count += 1
                num //= 2
            res.append(count)
        return res
