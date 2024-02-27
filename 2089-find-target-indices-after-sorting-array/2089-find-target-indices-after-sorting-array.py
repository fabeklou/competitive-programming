class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        list_index = []
        
        for index in range(len(nums)):
            if nums[index] == target:
                list_index.append(index)

        return list_index
