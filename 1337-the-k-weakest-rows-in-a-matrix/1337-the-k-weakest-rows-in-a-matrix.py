import heapq
class Node:
    def __init__(self,value, priority):
        self.value = value
        self.priority = priority
        
    def __lt__(self, other_node):
        if self.priority == other_node.priority:
            return self.value < other_node.value
        return self.priority < other_node.priority
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [Node(i,sum(row)) for i,row in enumerate(mat)]
        heapq.heapify(arr)
        print(arr)
        l = [heapq.heappop(arr).value for _ in range(k)]
        return l
        