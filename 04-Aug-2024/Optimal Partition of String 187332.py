# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        count = 1
        for char in s:
            if char in visited:
                visited.clear()
                count += 1
            visited.add(char)
        return count
