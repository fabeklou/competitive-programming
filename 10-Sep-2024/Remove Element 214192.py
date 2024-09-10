# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_non_val = ptr = len(nums) - 1
        k = 0
        while ptr >= 0:
            if nums[last_non_val] == val and nums[ptr] == val:
                last_non_val -= 1
            elif nums[ptr] == val:
                nums[ptr], nums[last_non_val] = nums[last_non_val], nums[ptr]
                last_non_val -= 1
            else:
                k += 1
            ptr -= 1
        return k
