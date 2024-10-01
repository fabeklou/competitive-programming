# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequencyMap = Counter(nums)
        limit = len(nums) // 3
        return [ num for num, occ in frequencyMap.items() if occ > limit ]
