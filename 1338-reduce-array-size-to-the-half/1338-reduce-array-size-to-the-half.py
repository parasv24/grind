class Node:
    def __init__(self, val, fre):
        self.val = val
        self.fre = fre
    def __lt__(self, other):
        return self.fre > other.fre

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mp = {}
        for el in arr:
            val = mp.get(el ,0)
            mp[el] = val +1
        nodes = []
        for key , val in mp.items():
            nodes.append(Node(key, val))
        heapify(nodes)
        size = len(arr)
        ans = 0
        curr_size = 0
        while(len(nodes)) > 0:
            node = heappop(nodes)
            ans+=1
            curr_size += node.fre
            if curr_size *2 >= size:
                break
        return ans
            
        
        