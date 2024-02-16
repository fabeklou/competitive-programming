class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count frequency of character to identify non-repeating characters
        frequence = Counter(s)

        # Iterate over the string to find the first non-repeating character
        for index, char in enumerate(s):
            # A non-repeating character is a key with value 1 in the frequence dict
            if frequence[char] == 1:
                # return index of the non-repeating character found
                return index

        # return -1 in case any non-repeating character was found
        return -1
