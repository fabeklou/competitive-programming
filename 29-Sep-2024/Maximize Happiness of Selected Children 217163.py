# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        count = 0
        for index, child in enumerate(happiness):
            if index == k:
                break
            count += max(child - index, 0)
        return count
