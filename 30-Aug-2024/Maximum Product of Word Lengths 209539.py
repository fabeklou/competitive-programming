# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ws = [set(w) for w in words]
        max_prod = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(ws[i] ^ ws[j]) == len(ws[i]) + len(ws[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod
