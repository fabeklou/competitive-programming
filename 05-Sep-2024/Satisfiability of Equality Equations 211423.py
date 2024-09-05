# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key=lambda x: x[1], reverse=True)
        root = [i for i in range(26)]
        size = [1] * 26

        def find(char):
            if char == root[char]:
                return char
            root[char] = find(root[char])
            return root[char]

        def union(char1, char2):
            root1, root2 = find(char1), find(char2)
            if root1 == root2:
                return
            if size[root1] > size[root2]:
                root[root2] = root1
                size[root1] += size[root2]
            else:
                root[root1] = root2
                size[root2] += size[root1]

        for eq in equations:
            # a: 97
            a, b = ord(eq[0]) - 97, ord(eq[-1]) - 97
            if eq[1] == '=':
                union(a, b)
                continue
            if find(a) == find(b):
                return False

        return True
