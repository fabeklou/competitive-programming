# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        adjs = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                adjs.append((i, i+1))
        for i, j in adjs:
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    s[i] = s[j] = ""
                    i -= 1
                    j += 1
                elif s[i] == "":
                    i -= 1
                elif s[j] == "":
                    j += 1
                else:
                    break
        return "".join([c for c in s if c!=""])
