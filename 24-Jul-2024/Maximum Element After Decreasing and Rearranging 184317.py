# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for index in range(len(arr) - 1):
            if arr[index + 1] - arr[index] > 1:
                arr[index + 1] = arr[index] + 1
        return arr[-1]
