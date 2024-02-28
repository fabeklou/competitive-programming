class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = sorted(zip(heights, names),
                        key = lambda item: item[0], reverse=True)
        return [name for height, name in output]
