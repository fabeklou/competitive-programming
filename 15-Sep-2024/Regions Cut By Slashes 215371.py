# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        matrix = [[0] * len(grid) * 3 for _ in range(len(grid) * 3)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix)

        def dfs(row, col):
            for r, c in directions:
                if inbound(row + r, col + c) and matrix[row + r][col + c] == 0:
                    matrix[row + r][col + c] = 1
                    dfs(row + r, col + c)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                r, c = i * 3, j * 3
                if grid[i][j] == '\\':
                    matrix[r][c] = matrix[r+1][c+1] = matrix[r+2][c+2] = 1
                elif grid[i][j] == '/':
                    matrix[r+2][c] = matrix[r+1][c+1] = matrix[r][c+2] = 1

        regions = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    regions += 1
                    dfs(i, j)

        return regions