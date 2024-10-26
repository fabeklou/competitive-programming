# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        has_odd = False
        palindrome_length = 0
        for _, value in freq.items():
            if value % 2:
                palindrome_length += (value - 1)
                has_odd = True
            else:
                palindrome_length += value
        return palindrome_length + 1 if has_odd else palindrome_length
