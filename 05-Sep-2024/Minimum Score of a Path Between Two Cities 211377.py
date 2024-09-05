# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minimumScore = float('inf')
        root = [i for i in range(n + 1)]
        score = [1] * (n + 1)

        def find(city):
            if city == root[city]:
                return city
            root[city] = find(root[city])
            return root[city]

        def union(cityA, cityB):
            originA, originB = find(cityA), find(cityB)
            if originA == originB:
                return
            if score[originA] > score[originB]:
                root[originB] = originA
                score[originA] += score[originB]
            else:
                root[originA] = originB
                score[originB] += score[originA]

        for cityA, cityB, distance in roads:
            union(cityA, cityB)

        for cityA, cityB, distance in roads:
            if find(cityA) == find(1):
                minimumScore = min(minimumScore, distance)

        return minimumScore
