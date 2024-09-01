# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        left = right = xor = 0
        for num in nums:
            xor ^= num
        mask = xor & ~(xor - 1)
        for num in nums:
            if num & mask:
                left ^= num
            else:
                right ^= num
        return [left, right]
