class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        clg = ''
        for chr in s:
            if chr in '{([':
                stack += chr
            else:
                clg = '{' if chr is '}' else '[' if chr is ']' else '('
            
                if stack and stack[-1] == clg:
                    stack = stack[:-1]
                else:
                    return False
        return len(stack) == 0
