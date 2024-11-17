# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lps = deque([0])
        rps = deque([0])
        for i in range(len(nums)):
            lps.append(lps[-1] + nums[i])
            rps.appendleft(rps[0] + nums[len(nums) - i - 1])
        lps.append(0)
        rps.appendleft(0)
        return [abs(lps[i-1] - rps[i+1]) for i in range(1, len(nums) + 1)]