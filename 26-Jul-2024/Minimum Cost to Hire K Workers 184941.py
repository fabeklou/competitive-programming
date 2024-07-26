# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratios = [(i, wage[i] / quality[i]) for i in range(len(quality))]
        ratios.sort(key=lambda x: x[1])
        least_amount = float('+inf')
        qualities = 0
        max_heap = []

        for index, curr_ratio in ratios:
            curr_quality, curr_wage = quality[index], wage[index]

            if len(max_heap) < k:
                heappush(max_heap, -curr_quality)
                qualities += curr_quality
            elif len(max_heap) == k and -max_heap[0] > curr_quality:
                qualities += heapreplace(max_heap, -curr_quality)
                qualities += curr_quality

            if len(max_heap) == k:
                least_amount = min(least_amount, qualities * curr_ratio)

        return least_amount
