class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num >= 0]
        negative = [num for num in nums if num < 0]
        rearranged = []
        
        for pos, neg in zip(positive, negative):
            rearranged += [pos, neg]
        
        return rearranged
