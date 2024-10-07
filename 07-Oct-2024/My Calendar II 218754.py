# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:
    def __init__(self):
        self.one = []
        self.two = []

    def book(self, start: int, end: int) -> bool:
        for st, nd in self.two:
            if not (start >= nd or end <= st):
                return False

        for st, nd in self.one:
            if not (start >= nd or end <= st):
                self.two.append((max(start, st), min(end, nd)))

        self.one.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)