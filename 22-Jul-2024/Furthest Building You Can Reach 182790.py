# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for index in range(len(heights) - 1):
            diff = heights[index + 1] - heights[index]

            if diff > 0:
                heappush(min_heap, diff)

                if len(min_heap) > ladders:
                    bricks -= heappop(min_heap)

                    if bricks < 0:
                        return index

        return len(heights) - 1
