# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        xor = 0
        for num in arr:
            xor ^= num
            prefix.append(xor)
        result = []
        for l, r in queries:
            result.append(prefix[l] ^ prefix[r+1])
        return result
