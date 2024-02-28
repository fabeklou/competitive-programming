class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute force approach
        # Time O(n*n)  &  space O(1)
        
        output = []
        size = len(nums)
        
        for i in range(size):
            count = 0
            for j in range(size):
                if nums[i] > nums[j]:
                    count += 1
            output.append(count)

        return output
