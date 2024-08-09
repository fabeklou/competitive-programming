# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return 0
        target = total // 2

        values = set([0])
        for num in nums:
            for value in tuple(values):
                values.add(value + num)
                values.add(num)

        return target in values
