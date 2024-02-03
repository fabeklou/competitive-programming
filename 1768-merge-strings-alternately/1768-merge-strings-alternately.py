class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        merged = ''

        for idx in range(len1 if len1 >= len2 else len2):
            if idx < len1:
                merged += word1[idx]
            if idx < len2:
                merged += word2[idx]
        return merged