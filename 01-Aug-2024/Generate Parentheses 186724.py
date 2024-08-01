# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def is_valid(parentheses):
            eq = 0
            for p in parentheses:
                if p == '(':
                    eq += 1
                    continue
                eq -= 1
                if eq < 0:
                    return False
            return eq == 0

        def bt(num, curr, left, right):
            if num == 0:
                if is_valid(curr):
                    result.append(curr[:])
                return
            curr.append('(')
            bt(num-1, curr, left + 1, right)
            curr.pop()
            if left > right:
                curr.append(')')
                bt(num-1, curr, left, right + 1)
                curr.pop()
        
        bt(n * 2, [], 0, 0)

        return [''.join(item) for item in result]
