# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        choices = [(0, -4), (3, -1), (1, -3), (2, -2)]
        min_diff = float('+inf')
        for x, y in choices:
            min_diff = min(min_diff, nums[y] - nums[x])
        return min_diff
