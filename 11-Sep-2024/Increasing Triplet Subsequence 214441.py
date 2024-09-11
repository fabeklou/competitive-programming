# Problem: Increasing Triplet Subsequence - https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = y = float('inf')
        for num in nums:
            if x > num:
                x = num
            elif x < num < y:
                y = num
            elif x < y < num:
                return True
        return False
