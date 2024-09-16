# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        hsetAllowed = set(allowed)
        for word in words:
            for char in set(word):
                if char not in hsetAllowed:
                    break
            else:
                count += 1
        return count
