class MinStack:

    def __init__(self):
        self.stck = []
        

    def push(self, val: int) -> None:
        if not self.stck:
            self.stck.append([val, val])
        else:
            x, mini = self.stck[-1]
            self.stck.append([val, min(mini, val)])
        

    def pop(self) -> None:
        if self.stck:
            self.stck.pop()
        

    def top(self) -> int:
        if self.stck:
            return self.stck[-1][0]
        

    def getMin(self) -> int:
        if self.stck:
            return self.stck[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()