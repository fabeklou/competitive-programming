class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # find the max subarray sum using Kadane's Algo
        runnSum=-1
        maxSum=float(\-inf\)
        for num in nums:
            if runnSum<0:
                runnSum=num
            else:
                runnSum+=num
            maxSum=max(maxSum,runnSum)
        return maxSum
