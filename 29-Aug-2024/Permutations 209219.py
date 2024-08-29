# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def bt(curr, mask):
            if len(curr) == len(nums):
                return permutations.append(curr[:])
            for index in range(len(nums)):
                if mask & (1 << index) == 0:
                    curr.append(nums[index])
                    mask |= (1 << index)
                    bt(curr, mask)
                    curr.pop()
                    mask &= ~(1 << index)
        bt([], 0)
        return permutations

