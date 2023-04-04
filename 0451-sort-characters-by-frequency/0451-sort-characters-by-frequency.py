class Node:
    def __init__(self, val, fre):
        self.value = val
        self.fre = fre
    def __lt__(self, other):
        return self.fre > other.fre
    
class Solution:
    def frequencySort(self, s: str) -> str:
        ls = list(s)
        mp = {}
        for el in ls:
            val = mp.get(el, 0)
            mp[el] = val +1
        nodes = []
        for key, val in mp.items():
            nodes.append(Node(key, val))
        heapify(nodes)
        ans = ""
        while(len(nodes)>0):
            node = heappop(nodes)
            ans += node.value * node.fre
        return ans