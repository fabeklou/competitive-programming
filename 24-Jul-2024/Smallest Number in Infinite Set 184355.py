# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [num for num in range(1, 1001)]
        heapify(self.heap)
        self.hash_set = set(self.heap)

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heappop(self.heap)
            self.hash_set.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num not in self.hash_set:
            heappush(self.heap, num)
            self.hash_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)