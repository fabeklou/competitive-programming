# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        dq = deque(costs)
        left = []
        right = []
        total_cost = 0

        for _ in range(candidates):
            if dq:
                heappush(left, dq.popleft())
            if dq:
                heappush(right, dq.pop())

        while k and (left or right):
            if left and right:
                if left[0] <= right[0]:
                    total_cost += heappop(left)
                    if dq:
                        heappush(left, dq.popleft())
                else:
                    total_cost += heappop(right)
                    if dq:
                        heappush(right, dq.pop())
            elif left:
                total_cost += heappop(left)
            else:
                total_cost += heappop(right)

            k -= 1

        return total_cost
