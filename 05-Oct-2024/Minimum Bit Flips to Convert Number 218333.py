# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diffs = 0
        while start or goal:
            if start & 1 != goal & 1:
                diffs += 1
            start >>= 1
            goal >>= 1
        return diffs
