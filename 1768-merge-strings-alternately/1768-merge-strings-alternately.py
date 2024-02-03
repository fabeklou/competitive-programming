class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        longest = len_w1 if len_w1 >= len_w2 else len_w2
        
        merged = ''
        for i in range(longest):
            if i < len_w1:
                merged += word1[i]
            if i < len_w2:
                merged += word2[i]
        return merged