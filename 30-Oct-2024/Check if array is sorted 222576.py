# Problem: Check if array is sorted - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        return sorted(arr) == arr