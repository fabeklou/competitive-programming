# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(idx, total, memo):
            if idx == len(nums):
                return 1 if target == total else 0
            if (idx, total) in memo: return memo[(idx, total)]
            neg = dp(idx + 1, total - nums[idx], memo)
            pos = dp(idx + 1, total + nums[idx], memo)
            memo[(idx, total)] = neg + pos
            return memo[(idx, total)]
        return dp(0, 0, {})
