class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bruite force approach: sum and set
        # time O(n) & space O(n)
        sum_all = sum(nums)
        sum_set = sum(set(nums))
        return sum_set*2 - sum_all
