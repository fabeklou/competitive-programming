class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time O(n)  &  space O(n)
        digits_char = map(str, digits)
        num = int(''.join(digits_char))
        return [int(c) for c in str(num + 1)]
