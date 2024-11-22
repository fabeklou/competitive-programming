# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lh, rh = [], []
        for index in range(len(arrays)):
            mini, maxi = arrays[index][0], arrays[index][-1]
            heappush(lh,[mini, index])
            heappush(rh, [-maxi, index])
        mini, maxi = lh[0][0], -rh[0][0]
        value = 0
        print(lh, rh)
        for index in range(len(arrays)):
            maxLeft = maxRight = 0
            if lh[0][1] != rh[index][1]:
                maxLeft = abs(lh[0][0] - (-rh[index][0]))
            if rh[0][1] != lh[index][1]:
                maxRight = abs((-rh[0][0]) - lh[index][0])
            value = max(maxLeft, maxRight, value)
        return value
 