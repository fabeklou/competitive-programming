# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for num in nums:
            colors[num] += 1

        color_index = index = 0
        while index < len(nums):
            if colors[color_index] == 0:
                color_index += 1
                continue
            nums[index] = color_index
            colors[color_index] -= 1
            index += 1
