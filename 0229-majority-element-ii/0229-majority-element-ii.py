class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute force solution using a hashMap
        #   time O(n)  &  space O(n)
        frequencyMap = Counter(nums)
        limit = len(nums) // 3
        return [ num for num, occ in frequencyMap.items() if occ > limit ]

        # optimized solution using <Boyer-Moore Voting Algorithm>
        # len([result]) <= 2
        #   time O(n)  &  space O(1)
        """To implement later
        """