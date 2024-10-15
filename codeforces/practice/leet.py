class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratios = [(i, wage[i] / quality[i]) for i in range(len(quality))]
        ratios.sort(key=lambda x: x[1], reverse=True)
        least_amount = float('+inf')

        for curr_index, (lead_index, lead_ratio) in enumerate(ratios):
            max_heap = [-wage[lead_index]]
            curr_amount = -max_heap[0]
            if len(ratios) - curr_index < k:
                break
            for _index in range(curr_index + 1, len(ratios)):
                mate_index, _ = ratios[_index]
                mate_wage = lead_ratio * quality[mate_index]

                if len(max_heap) < k:
                    curr_amount += mate_wage
                    heappush(max_heap, -mate_wage)
                elif len(max_heap) == k and -max_heap[0] > mate_wage:
                    curr_amount += heapreplace(max_heap, -mate_wage)
                    curr_amount += mate_wage
            amounts.append(curr_amount)
            if len(max_heap) == k:
                least_amount = min(least_amount, curr_amount)

        return least_amount
