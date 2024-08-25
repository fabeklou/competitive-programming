# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(index, robbedFirst):
            if index >= len(nums) - 1 and robbedFirst:
                return nums[0]
            if index >= len(nums):
                return 0
            if (index, robbedFirst) in cache:
                return cache[(index, robbedFirst)]

            rob = nums[index] + dp(index + 2, robbedFirst)
            skip = dp(index + 1, robbedFirst)
            cache[(index, robbedFirst)] = max(rob, skip)

            return cache[(index, robbedFirst)]

        return max(dp(2, True), dp(1, False))
