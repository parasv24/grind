class MyCalendarThree:

    def __init__(self):
        self.mp = {}
        

    def book(self, startTime: int, endTime: int) -> int:
        self.mp[startTime] = self.mp.get(startTime, 0) + 1
        self.mp[endTime] = self.mp.get(endTime, 0) - 1
        cnt = 0
        ans = 0
        for key in sorted(self.mp.keys()):
            cnt += self.mp[key]
            ans = max(ans, cnt)
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)