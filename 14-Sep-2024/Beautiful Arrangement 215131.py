# Problem: Beautiful Arrangement - https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        permutations = 0
        visited = set()

        def isValid(index, num):
            return index % num == 0 or num % index == 0

        def bt(nums):
            nonlocal permutations
            if len(nums) == n:
                permutations += 1
                return

            for nei in range(1, n + 1):
                if nei in visited or not isValid(len(nums)+1, nei):
                    continue
                nums.append(nei)
                visited.add(nei)
                bt(nums)
                visited.remove(nums.pop())

        bt([])
        return permutations 
