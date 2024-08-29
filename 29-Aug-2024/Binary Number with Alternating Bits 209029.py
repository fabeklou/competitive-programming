# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        expected = 1 if n % 2 else 0
        while n:
            if not n % 2 == expected:
                return False
            n >>= 1
            expected ^= 1
        return True
