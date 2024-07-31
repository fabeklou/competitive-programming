# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        incoming = [0] * n

        for parent, child in edges:
            graph[parent].append(child)
            incoming[child] += 1
        
        dq = deque()
        for index, count in enumerate(incoming):
            if count == 0:
                dq.append(index)

        result = [set() for _ in range(n)]

        while dq:
            parent = dq.popleft()

            for child in graph[parent]:
                incoming[child] -= 1
                result[child].add(parent)
                result[child] |= result[parent]
                if incoming[child] == 0:
                    dq.append(child)

        return [sorted(list(s)) for s in result]
