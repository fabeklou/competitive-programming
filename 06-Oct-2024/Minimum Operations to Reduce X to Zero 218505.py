# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        total_sum = sum(nums)
        curr_sum = 0
        res = float('+inf')
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > abs(total_sum - x):
                curr_sum -= nums[left]
                left += 1
            if total_sum - curr_sum == x:
                res = min(len(nums) - (right - left) - 1, res)
        return res if res != float('+inf') else -1
