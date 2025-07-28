# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise = 0
        subsets = 1
        for n in nums:
            max_bitwise |= n
        for r in range(1, len(nums)):
            for nums_subset in combinations(nums, r):
                curr = 0
                for n in nums_subset:
                    curr |= n
                if curr == max_bitwise:
                    subsets += 1
        return subsets
