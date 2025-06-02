# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        triangles = 0
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                left, right = j + 1, len(nums) - 1
                a, b = nums[i], nums[j]
                count = 0
                while left <= right:
                    c_index = left + (right - left) // 2
                    c = nums[c_index]
                    if a + b > c and a + c > b and b + c > a:
                        count = c_index - j
                        left = c_index + 1
                    else:
                        right = c_index - 1
                triangles += count
        return triangles
 