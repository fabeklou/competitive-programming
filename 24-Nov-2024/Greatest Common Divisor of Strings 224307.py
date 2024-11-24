# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ptr = 0
        for a, b in zip_longest(str1, str2, fillvalue=None):
            if a != b:
                break
            ptr += 1
        x = str1[:ptr]
        while x:
            if (x * (len(str1) // len(x)) == str1) and (x * (len(str2) // len(x)) == str2):
                break
            x = x[:-1]
        return x
