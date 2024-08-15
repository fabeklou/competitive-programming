# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OG = obstacleGrid  # aliasing

        def inbound(row, col):
            return 0 <= row < len(OG) and 0 <= col < len(OG[0])

        def memo(grid, row, col, cache):
            if not inbound(row, col) or grid[row][col] == 1:
                return 0

            if row == len(OG) - 1 and col == len(OG[0]) -1:
                return 1

            if cache[row][col] == -1:
                cache[row][col] = memo(grid, row+1, col, cache) + memo(grid, row, col+1, cache)
            return cache[row][col]

        return memo(OG, 0, 0, [[-1] * len(OG[0]) for _ in range(len(OG))])
