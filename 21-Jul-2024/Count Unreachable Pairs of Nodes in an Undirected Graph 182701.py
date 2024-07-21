# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        groups = []
        visited = set()
        for node in range(n):
            curr_group = 1
            if node in visited:
                continue
            visited.add(node)
            dq = deque([node])
            while dq:
                node = dq.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        curr_group += 1
                        dq.append(neighbor)
                        visited.add(neighbor)
            groups.append(curr_group)

        max_sep = n * (n - 1) // 2
        for g in groups:
            dim = g * (g - 1) // 2
            max_sep -= dim
        return max_sep
        