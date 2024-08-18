# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        keyboard = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        def bt(index, curr):
            if len(digits) == len(curr):
                res.append(''.join(curr))
                return
            
            for ch in keyboard[digits[index]]:
                curr.append(ch)
                bt(index + 1, curr)
                curr.pop()

        bt(0, [])
        return res
