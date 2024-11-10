# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        ptr = 0
        while ptr < len(s):
            if not stk or stk[-1][0] != s[ptr]:
                stk.append([s[ptr], 1])
            else:
                lastChar, charCount = stk[-1]
                if charCount + 1 == k:
                    stk.pop()
                else:
                    stk[-1][1] += 1
            ptr += 1
        return "".join([currChr * chrCount for currChr, chrCount in stk])
