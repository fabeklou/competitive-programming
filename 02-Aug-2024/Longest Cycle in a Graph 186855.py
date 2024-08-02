# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        W, G, B = -1, 0, 1
        max_length = -1
        states = [W] * len(edges)

        def dfs(node, path):
            states[node] = G
            path.append(node)
            nei = edges[node]

            if nei == -1:
                states[node] = B
                return False
            
            if states[nei] == G:
                path.append(nei)
                return True
            if states[nei] == W and dfs(nei, path):
                return True

            states[node] = B
            return False

        for node, nei in enumerate(edges):
            if nei == -1 or states[node] != W:
                continue
            path = []
            if dfs(node, path):
                size = len(path) - path.index(path[-1]) - 1
                max_length = max(max_length, size)

        return max_length
