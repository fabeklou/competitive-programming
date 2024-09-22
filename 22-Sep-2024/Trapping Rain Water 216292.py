# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []

        def getWater(n, heights):
            w = 0
            stk.clear()
            for pos in range(n):
                if not stk or (len(stk) == 1 and stk[0] <= heights[pos]):
                    if stk:
                        stk.pop()
                    stk.append(heights[pos])
                    continue
                stk.append(heights[pos])
                if stk[-1] >= stk[0]:
                    right = stk[-1]
                    diff = min(right, stk[0])
                    while stk:
                        w += max(0, diff - stk.pop())
                    stk.append(right)
            return w

        water = 0
        water = getWater(len(height), height)
        if len(stk) > 2:
            water += getWater(len(stk), stk[::-1])
        return water
