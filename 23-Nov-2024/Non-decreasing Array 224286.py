# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for index in range(len(nums) - 1):
            if nums[index] <= nums[index + 1]:
                continue
            if modified:
                return False
            if index == 0 or nums[index + 1] >= nums[index - 1]:
                nums[index] = nums[index + 1]
            else:
                nums[index + 1] = nums[index]
            modified = True
        return True
