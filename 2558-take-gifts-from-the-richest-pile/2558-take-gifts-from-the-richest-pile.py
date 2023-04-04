import heapq
class Node:
    def __init__(self, val):
        self.value = val
        
    def __lt__(self, other_node):
        return self.value > other_node.value
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_nodes = [Node(el) for el in gifts]
        heapq.heapify(gifts_nodes)
        for i in range(k):
            temp = heapq.heappop(gifts_nodes)
            val = isqrt(temp.value)
            heapq.heappush(gifts_nodes, Node(val))
        ans = 0
        for i in gifts_nodes:
            ans += i.value
        return ans