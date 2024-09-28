# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        left, right = intervals[0]
        for pos in range(len(intervals)):
            if right >= intervals[pos][0]:
                left = min(intervals[pos][0], left)
                right = max(intervals[pos][1], right)
            else:
                res.append([left, right])
                left, right = intervals[pos]
        res.append([left, right])
        return res
