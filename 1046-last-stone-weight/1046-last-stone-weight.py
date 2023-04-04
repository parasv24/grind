import heapq
class Node:
    def __init__(self, val):
        self.value = val
    def __lt__(self, other):
        return self.value > other.value

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nodes = [Node(i) for i in stones]
        heapq.heapify(nodes)
        while len(nodes) > 1:
            y = heapq.heappop(nodes).value
            x = heapq.heappop(nodes).value
            if y == x:
                continue
            else:
                heapq.heappush(nodes, Node(y-x))
        return nodes[0].value if len(nodes) == 1 else 0