class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for ope in operations:
            if ope in '++X++':
                result += 1
            else:
                result -= 1
        return result