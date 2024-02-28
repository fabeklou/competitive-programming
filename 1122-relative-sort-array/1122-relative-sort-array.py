class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hmap = {}
        size = len(arr2)

        for index, num in enumerate(arr2):
            hmap[num] = index

        arr1.sort(key = lambda num: hmap[num] if num in hmap else num + size)
        return arr1
