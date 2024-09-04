# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [v for v in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)
        target_edge = []

        def find(v):
            if v == root[v]:
                return v
            root[v] = find(root[v])
            return root[v]
        
        def union(root_v1, root_v2):
            if root[root_v1] > root[root_v2]:
                root[root_v2] = root_v1
                size[root_v1] +=  size[root_v2]
            else:
                root[root_v1] = root_v2
                size[root_v2] += size[root_v1]

        for v1, v2 in edges:
            root_v1, root_v2 = find(v1), find(v2)

            if root_v1 == root_v2:
                target_edge = [v1, v2]
                continue

            union(root_v1, root_v2)

        return target_edge
