# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def bt(index, path):
            if len(path) > 1:
                result.add(tuple(path))
            for i in range(index, len(nums)):
                if not path or path[-1] <= nums[i]:
                    bt(i + 1, path + nums[i:i+1])

        result = set()
        bt(0, [])
        return list(result)

        