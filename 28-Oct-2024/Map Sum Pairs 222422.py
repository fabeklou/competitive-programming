# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.mso = {}

    def insert(self, key: str, val: int) -> None:
        self.mso[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        for k, v in self.mso.items():
            if k.startswith(prefix):
                s += v
        return s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)