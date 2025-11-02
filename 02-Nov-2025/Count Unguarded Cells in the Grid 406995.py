# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def set_guarded_cells(self, matrix, row, col):
        def is_inbound(curr_row, curr_col):
            return 0 <= curr_row < len(matrix)  and 0 <= curr_col < len(matrix[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for r, c in directions:
            next_row, next_col = row + r, col + c
            while is_inbound(next_row, next_col) and matrix[next_row][next_col] in {1, -1}:
                matrix[next_row][next_col] = -1
                next_row += r
                next_col += c
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # -1 -> guarded
        # 0 -> guard
        # 1 -> free cell
        # 2 -> wall
        result = 0
        matrix = [[1] * n for _ in range(m)]
        for row, col in walls:
            matrix[row][col] = 2
        for row, col in guards:
            matrix[row][col] = 0
        for row, col in guards:
            self.set_guarded_cells(matrix, row, col)
        for row in matrix:
            result += row.count(1)
        return result
    