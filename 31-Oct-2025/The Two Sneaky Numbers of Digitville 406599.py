# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        hash_set = set()
        for n in nums:
            if n in hash_set:
                result.append(n)
            hash_set.add(n)
        return result
