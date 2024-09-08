# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = [i for i in range(len(stones))]
        size = [1] * len(stones)

        def find(s):
            if s == root[s]:
                return s
            root[s] = find(root[s])
            return root[s]
        
        def union(s1, s2):
            root1, root2 = find(s1), find(s2)
            if root1 == root2:
                return
            if size[root1] > size[root2]:
                root[root2] = root1
                size[root1] += size[root2]
            else:
                root[root1] = root2
                size[root2] += size[root1]

        conflicts_col = {}
        conflicts_row = {}

        for index, (x, y) in enumerate(stones):
            if x not in conflicts_row:
                conflicts_row[x] = [index]
            else:
                for nei in conflicts_row[x]:
                    union(nei, index)
                conflicts_row[x].append(index)

            if y not in conflicts_col:
                conflicts_col[y] = [index]
            else:
                for nei in conflicts_col[y]:
                    union(nei, index)
                conflicts_row[x].append(index)

        return len(stones) - len({ find(s) for s in range(len(stones)) })
