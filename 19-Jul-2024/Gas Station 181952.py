# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        dist = [gas[i] - cost[i] for i in range(len(gas))]

        reservoir = 0
        starting_position = 0

        for position in range(len(dist)):
            reservoir += dist[position]
            if reservoir < 0:
                starting_position = position + 1
                reservoir = 0

        return starting_position
