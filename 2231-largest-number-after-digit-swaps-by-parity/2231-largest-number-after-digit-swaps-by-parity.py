import heapq
class Node:
    def __init__(self, val):
        self.value = val
    def __lt__(self, other):
        return self.value > other.value
class Solution:
    def largestInteger(self, num: int) -> int:
        nums= list(str(num))
        print(nums)
        nums = [int(el) for el in nums]
        print(nums)
        odds = [Node(el) for el in nums if el % 2 != 0]
        evens = [Node(el) for el in nums if el % 2 == 0]
        heapq.heapify(odds)
        heapq.heapify(evens)
        ans = ""
        for el in nums:
            val = heapq.heappop(odds) if el %2 != 0 else heapq.heappop(evens)
            ans += str(val.value)
        return int(ans)
        