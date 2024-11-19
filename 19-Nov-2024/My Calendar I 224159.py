# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for left, right in self.calendar:
            if not (right <= startTime or endTime <= left):
                return False
        self.calendar.append((startTime, endTime))
        return True
