class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] == nums[j]:
                    count += 1
        return count