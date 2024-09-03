# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []

        matrix = []
        for row in range(m):
            skip = row * n
            matrix.append(original[skip : skip + n])
        return matrix
