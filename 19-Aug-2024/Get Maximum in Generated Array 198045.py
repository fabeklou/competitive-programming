# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        if len(nums) > 1: nums[1] = 1
        for index in range(n):
            if 2 <= 2 * index <= n:
                nums[2 * index] = nums[index]
            if 2 <= 2 * index + 1 <= n:
                nums[2 * index + 1] = nums[index] + nums[index + 1]
        return max(nums)
