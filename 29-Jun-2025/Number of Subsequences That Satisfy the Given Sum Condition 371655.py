# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        for min_index, num in enumerate(nums):
            if (num * 2 > target):
                break
            # binary search to find a valid subarray
            left, right, max_index = min_index, len(nums) - 1, min_index
            while left <= right:
                mid = left + (right - left) // 2
                if (nums[mid] + nums[min_index] <= target):
                    max_index = mid
                    left = mid + 1
                else:
                    right = mid - 1
            result += 2**(max_index - min_index)
        return result % (10**9 + 7)
