class Solution:
    def isPalindrome(self, x: int) -> bool:
        return f'{x}' == f'{x}'[::-1]