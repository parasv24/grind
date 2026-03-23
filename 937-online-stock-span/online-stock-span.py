class StockSpanner:

    def __init__(self):
        self.stck = []
        self.idx = {}
        self.counter = 0
        

    def next(self, price: int) -> int:
        ans = 1
        self.counter += 1
        if len(self.stck) > 0:
            if self.stck[-1] > price:
                ans = 1
            else:
                while len(self.stck) > 0 and self.stck[-1] <= price:
                    self.stck.pop()
                ans = self.counter - self.idx[self.stck[-1]] if len(self.stck) > 0 else self.counter
        self.stck.append(price)
        self.idx[price] = self.counter
        return ans
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)