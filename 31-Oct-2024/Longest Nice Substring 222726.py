# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ['', 0]

        def dnc(strArr):
            if len(strArr) < 2 or len(strArr) <= res[1]:
                return

            niceTest = defaultdict(set)
            for char in strArr:
                niceTest[char.lower()].add(char)
            print(niceTest)
            for index, char in enumerate(strArr):
                if len(niceTest[char.lower()]) == 1:
                    dnc(strArr[:index])
                    dnc(strArr[index + 1:])
                    break
            else:
                if len(strArr) > res[1]:
                    res[0], res[1] = ''.join(strArr), len(strArr)

        
        dnc(list(s))
        niceStr = res[0]
        return niceStr
