class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using Boyer-Moore Majority Vote Algorithm
        #   time O(n)  &  space O(1)
        count, maj_elem = 0, 0
        for num in nums:
            if count == 0:
                # num may be our majority element
                maj_elem = num
            count += (1 if num == maj_elem else -1)
        return maj_elem
