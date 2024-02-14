class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        positions = {}
        
        for index, num in enumerate(nums):
            positions[num] = index
        
        for value, replace in operations:
            nums[positions[value]] = replace
            # value does not exists in list anymore so we should update it
            positions[replace] = positions[value]
            del positions[value]
        
        return nums
