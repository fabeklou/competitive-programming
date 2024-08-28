# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        complement, weight = 0, 1
        while num:
            if not num & 1:
                complement += weight
            num >>= 1
            weight *= 2
        return complement
