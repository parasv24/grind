class SeatManager:

    def __init__(self, n: int):
        self.ls = [i for i in range(1, n+1)]
        heapify(self.ls)        

    def reserve(self) -> int:
        return heappop(self.ls)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.ls, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)