class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
    def __lt__(self, other):
        return self.freq > other.freq

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mp = {}
        for el in roads:
            mp[el[0]] = mp.get(el[0], 0) + 1
            mp[el[1]] = mp.get(el[1], 0) + 1
        nodes = []
        for key, val in mp.items():
            nodes.append(Node(key, val))
        heapify(nodes)
        sums = 0
        while len(nodes) > 0:
            item = heappop(nodes)
            print(item.value, n)
            sums += n * item.freq
            n -= 1
        return sums
            
            
            
        
        