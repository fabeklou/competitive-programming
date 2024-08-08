# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dp(row, col, memo):
            if row == m or col == n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if memo[row][col] == -1:
                memo[row][col] = dp(row + 1, col, memo) + dp(row, col + 1, memo)
            return memo[row][col]

        return dp(0, 0, [[-1] * n for _ in range(m)])
