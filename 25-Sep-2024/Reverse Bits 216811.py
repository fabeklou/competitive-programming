# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        return int(('0' * (32 - len(bits)) + bits)[::-1], 2)
