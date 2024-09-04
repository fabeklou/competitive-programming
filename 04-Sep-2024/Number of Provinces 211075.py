# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        graph = [[] for _ in range(size)]

        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        visited = set()
        provinces = 0
        for node in range(size):
            if node not in visited:
                dfs(node)
                provinces += 1
        
        return provinces
