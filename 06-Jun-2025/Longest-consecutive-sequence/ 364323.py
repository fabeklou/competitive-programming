# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_set = set()
        longest_seq = 0
        for num in nums:
            if num - 1 not in nums_set and num not in start_set:
                seq_end = num
                start_set.add(num)
                while seq_end in nums_set:
                    seq_end += 1
                longest_seq = max(longest_seq, seq_end - num)
        return  longest_seq      
