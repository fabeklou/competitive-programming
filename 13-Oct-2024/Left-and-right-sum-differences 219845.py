# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        right = [0]
        for num in nums[:-1]:
            left.append(left[-1] + num)
        for num in nums[::-1][:-1]:
            right.append(right[-1] + num)
        right.reverse()
        return [abs(a - b) for a, b in zip(left, right)]
