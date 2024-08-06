# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        counts = [0, 0]
        
        for num in nums:
            counts[0], counts[1] = counts[1], max(num + counts[0], counts[1])

        return counts[1]       
