# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-n for n in nums]
        heapify(nums)
        for _ in range(k):
            largest = -heappop(nums)
            heappush(nums, -math.ceil(largest / 3))
            score += largest
        return score
