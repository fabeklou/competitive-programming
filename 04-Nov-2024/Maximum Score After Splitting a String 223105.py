# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        score = s[1:].count('1')
        if s[0] == '0': score += 1
        max_score = score
        for chr in s[1:len(s) - 1]:
            if chr == '0':
                score += 1
                max_score = max(max_score, score)
            else:
                score -= 1
        return max_score
