# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        flat, ans=[], []
        for i in mat:
            flat += i
        for i in range(r):
            ans+=[flat[i*c : i*c+c]]
        return ans
