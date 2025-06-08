# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def directions(i: int, j: int):
            return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        def in_bound(i: int, j: int):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        def dfs(i, j, index, visited):
            if index == len(word):
                return True
            for x, y in directions(i, j):
                if (x, y) not in visited and in_bound(x, y) and board[x][y] == word[index]:
                    visited.add((x,y))
                    if dfs(x, y, index + 1, visited):
                        return True
                    visited.remove((x,y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 1, {(i,j)}):
                    return True

        return False
