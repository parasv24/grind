class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.value > other.value
        return self.freq < other.freq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = {}
        for el in words:
            mp[el] = mp.get(el, 0) + 1
        nodes  = []
        for key , value in mp.items():
            nodes.append(Node(key, value))
        heap = nodes[:k]
        heapify(heap)
        for el in heap:
            print(el.value ,end = " ")
        for i in range(k, len(nodes)):
            # print(heap[0].freq, heap[0].value, nodes[i].freq, nodes[i].value)
            if heap[0].freq == nodes[i].freq and heap[0].value > nodes[i].value:
                heapreplace(heap, nodes[i])
            if heap[0].freq < nodes[i].freq:
                heapreplace(heap, nodes[i])
                
        heap.sort(key = lambda a: a.value)
        heap.sort(key = lambda a: -1 * a.freq)
        ans = [node.value for node in heap]
        return ans
                