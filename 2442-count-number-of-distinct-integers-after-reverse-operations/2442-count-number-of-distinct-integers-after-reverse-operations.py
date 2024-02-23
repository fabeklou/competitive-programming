class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # time O(n*m) & space O(n)
        for i in range(len(nums)):
            nums.append(self.reverseNumber(nums[i]))
        return len(set(nums))

    def reverseNumber(self, num):
        reversedNum = 0
        while num != 0:
            last_digit = num % 10
            reversedNum = (reversedNum * 10) + last_digit
            num //= 10
        return reversedNum
