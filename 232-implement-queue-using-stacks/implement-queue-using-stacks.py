class MyQueue:

    def __init__(self):
        self.stck = []
        

    def push(self, x: int) -> None:
        helper_stck = []
        while len(self.stck) > 0:
            helper_stck.append(self.stck.pop())
        self.stck = [x]
        while len(helper_stck) > 0:
            self.stck.append(helper_stck.pop())
        

    def pop(self) -> int:
        return self.stck.pop()
        

    def peek(self) -> int:
        return self.stck[-1] if not self.empty() else -1
        

    def empty(self) -> bool:
        return len(self.stck) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()