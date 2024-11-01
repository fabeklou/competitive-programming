# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        target_color = image[sr][sc]

        def inbound(row, col):
            return 0 <= row < len(image) and  0 <= col < len(image[0])

        def dfs(row, col):
            image[row][col] = color
            for r, c in directions:
                new_row, new_col = row + r, col + c
                if inbound(new_row, new_col) and image[new_row][new_col] == target_color and image[new_row][new_col] != color:
                    dfs(new_row, new_col)

        dfs(sr, sc)
        return image
