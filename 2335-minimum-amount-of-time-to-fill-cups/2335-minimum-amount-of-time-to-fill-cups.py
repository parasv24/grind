import heapq
class Node:
    def __init__(self, val):
        self.value = val
    def __lt__(self, other):
        return self.value > other.value 
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        nodes = [Node(node) for node in amount if node > 0]
        heapq.heapify(nodes)
        ans = 0
        while len(nodes) > 1:
            x = heapq.heappop(nodes)
            y = heapq.heappop(nodes)
            x.value -= 1
            y.value -= 1
            if x.value > 0:
                heapq.heappush(nodes, x)
            if y.value > 0:
                heapq.heappush(nodes, y)
            ans += 1
        if len(nodes) == 1:
            ans += nodes[0].value
        return ans