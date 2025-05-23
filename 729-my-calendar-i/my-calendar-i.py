class MyCalendar:

    def __init__(self):
        self.mp = {}

    def book(self, startTime: int, endTime: int) -> bool:
        self.mp[startTime] = self.mp.get(startTime, 0) + 1
        self.mp[endTime] = self.mp.get(endTime, 0) - 1
        cnt = 0
        for key in sorted(self.mp.keys()):
            cnt += self.mp[key]
            if cnt == 2:
                self.mp[startTime] -= 1
                self.mp[endTime] += 1
                return False
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)