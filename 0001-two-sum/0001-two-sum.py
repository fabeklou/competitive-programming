class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  brute force solution TC O(n²)  AS O(1)
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """

        #  better solution using a hashmap TC O(n)  AS O(n)
        hashmap = {}
        for index, num in enumerate(nums):
            rem = target - num
            if rem in hashmap:
                return [hashmap[rem], index]
            else:
                hashmap[num] = index
            