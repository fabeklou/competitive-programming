# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hset = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] in hset:
                nums[i] = 101
                k += 1
            hset.add(nums[i])
        nums.sort()
        return len(nums) - k
