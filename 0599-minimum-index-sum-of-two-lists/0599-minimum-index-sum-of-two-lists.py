class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1, dict2, union = {}, {}, {}
        result = []
        min_ = 0
        
        for index, tup in enumerate(zip_longest(list1, list2, fillvalue=None)):
            x, y = tup
            if not x is None:
                dict1[x] = index
            if not y is None:
                dict2[y] = index
        
        for string, index in dict2.items():
            if string in dict1:
                union[string] = index + dict1[string]
        
        min_ = min(union.values())
        
        for string, index in union.items():
            if index == min_:
                result.append(string)
        
        return result

        
        
