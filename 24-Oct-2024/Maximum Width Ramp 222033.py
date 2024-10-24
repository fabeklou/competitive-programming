# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = sorted(range(n), key=lambda i: nums[i])
        
        max_width = 0
        min_index = indices[0]
        
        for j in indices:
            min_index = min(min_index, j)
            max_width = max(max_width, j - min_index)
        
        return max_width
