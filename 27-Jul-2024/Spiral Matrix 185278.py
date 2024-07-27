# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dirirection = 0
        row = col = 0
        visited = set()

        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        while len(res) < len(matrix) * len(matrix[0]):
            if (row, col) not in visited:
                res.append(matrix[row][col])
                visited.add((row, col))

            r, c = directions[curr_dirirection % len(directions)]
            next_row, next_col = row + r, col + c
        
            if inbound(next_row, next_col) and (next_row, next_col) not in visited:
                row, col = next_row, next_col
            else:
                curr_dirirection += 1

        return res
