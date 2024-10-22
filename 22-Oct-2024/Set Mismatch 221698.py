# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        count = Counter(nums)
        for key, value in count.items():
            if value == 2:
                duplicate = key
                break
        return [duplicate, list(set(nums) ^ set(range(1, len(nums) + 1)))[0]]
