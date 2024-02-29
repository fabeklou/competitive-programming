class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        # Time O(n)  &  Space O(n)
        
        colors = [0, 0, 0]
        target = 0
        
        for num in nums:
            colors[num] += 1
        
        for index, color in enumerate(colors):
            for _ in range(color):
                nums[target] = index
                target += 1
