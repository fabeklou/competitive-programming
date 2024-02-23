class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hset_top = set("qwertyuiop")
        hset_middle = set("asdfghjkl")
        hset_bottom = set("zxcvbnm")
        result = []

        for word in words:
            hset_word = set(word.lower())
            if not hset_word - hset_top\
                or not hset_word - hset_middle\
                or not hset_word - hset_bottom:
                    result.append(word)
        
        return result
