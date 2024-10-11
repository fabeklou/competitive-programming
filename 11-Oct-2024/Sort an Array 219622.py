# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        sorted_nums = []
        while nums:
            sorted_nums.append(heappop(nums))
        return sorted_nums
