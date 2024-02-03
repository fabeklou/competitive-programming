class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_s = sorted(s)
        list_t = sorted(t)
        for i in range(len(s)):
            if list_s[i] != list_t[i]:
                return list_t[i]
        return list_t[-1]