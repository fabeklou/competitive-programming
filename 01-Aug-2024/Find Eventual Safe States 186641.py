# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        reversed_graph = [[] for _ in range(len(graph))]
        incoming = [0] * len(graph)
        dq = deque()

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reversed_graph[neighbor].append(node)
            incoming[node] = len(neighbors)
        
        for node, count in enumerate(incoming):
            if count == 0:
                dq.append(node)

        result = []
        while dq:
            node = dq.popleft()
            result.append(node)
            for neighbor in reversed_graph[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    dq.append(neighbor)

        result.sort()  
        return result
