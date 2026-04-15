class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        i = len(self.queue) - 1
        while i - 1 >= 0:
            self.queue[i], self.queue[i-1] = self.queue[i-1], self.queue[i]
            i -= 1
            

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()