# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [1] * (n + 1)
        nums[0] = 0
        for index in range(3, n + 1):
            nums[index] = sum(nums[index - 3 : index])
        return nums[-1]
