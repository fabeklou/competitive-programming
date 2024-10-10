# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top = sorted(list(freq.items()), key=lambda x : x[1], reverse=True)
        result = []
        for index in range(len(nums)):
            if index >= k:
                break
            result.append(top[index][0])
        return result
