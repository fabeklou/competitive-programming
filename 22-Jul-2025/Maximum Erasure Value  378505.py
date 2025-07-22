# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        visited = set()
        maximum_sum = visited_sum = 0
        for right in nums:
            while right in visited:
                visited_sum -= nums[left]
                visited.remove(nums[left])
                left += 1
            visited.add(right)
            visited_sum += right
            maximum_sum = max(maximum_sum, visited_sum)
        return maximum_sum
    