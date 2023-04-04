class Node:
    def __init__(self, val, fre):
        self.val = val
        self.fre = fre
    def __lt__(self, other):
        return self.fre < other.fre
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for el in nums:
            mp[el] = mp.get(el,0) + 1
        nodes = [Node(key, val) for key, val in mp.items()]
        if k > len(nodes):
            heapify(nodes)
            ans = [node.val for node in nodes]
        else:
            heap_nodes = nodes[:k]
            heapify(heap_nodes)
            for i in range(k, len(nodes)):
                if nodes[i].fre > heap_nodes[0].fre:
                    heapreplace(heap_nodes, nodes[i])
            ans = [node.val for node in heap_nodes]
        return ans