# Problem: Validate Stack Sequences - https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        po_idx = 0

        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[po_idx]:
                stack.pop()
                po_idx += 1

        return stack == []
