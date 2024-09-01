# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice, neg = 0, 0, 0
        for num in nums:
            mask = 1
            if num < 0: neg += 1
            num = num if num > 0 else -num
            while mask <= num:
                if num & mask:
                    if twice & mask:
                        once &= ~mask
                        twice &= ~mask
                    elif once & mask:
                        twice |= mask
                    else:
                        once |= mask
                mask <<= 1
        return once * (-1 if neg%3 else 1)
