class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwad, backward = '', ''

        for chr in s:
            if chr.isalnum():
                chr = chr.lower()
                forwad = chr + forwad
                backward = backward + chr

        return forwad == backward
