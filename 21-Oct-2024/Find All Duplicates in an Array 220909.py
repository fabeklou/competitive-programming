# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        once, twice = 0, 0
        result = []
        for num in nums:
            mask = 1
            mask <<= (num - 1)
            if mask & once:
                twice |= mask
            else:
                once |= mask
        for n in range(1, len(nums) + 1):
            if twice & 1:
                result.append(n)
            twice >>= 1
        return result
