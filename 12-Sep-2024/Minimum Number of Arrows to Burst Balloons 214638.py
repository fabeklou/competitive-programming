# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        target = points[0]
        arrows = 1
        for x, y in points[1:]:
            if x <= target[1]:
                continue
            arrows += 1
            target = [x, y]
        return arrows
