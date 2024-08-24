# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return '0'

        numbers = [str(num) for num in nums]
        numbers.sort(reverse=True)

        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if int(numbers[i] + numbers[j]) < int(numbers[j] + numbers[i]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
    
        return ''.join(numbers)
