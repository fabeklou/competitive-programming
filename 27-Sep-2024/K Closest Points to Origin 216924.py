# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heappush(min_heap, (-dist, x, y))
            if len(min_heap) > k:
                heappop(min_heap)
        return [item[1:] for item in min_heap]
