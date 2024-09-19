# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def canReach(psum, ones):
            for i in range(len(psum) - ones):
                if psum[i + ones] - psum[i] >= ones - k:
                    return True
            return False

        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)
        maxcons = 0
        left, right = 1, len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if canReach(psum, mid):
                left = mid + 1
                maxcons = mid
            else:
                right = mid - 1
        
        return maxcons
