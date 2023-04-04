import heapq
class Node:
    count = 1
    def __init__(self, val):
        self.value = val
    def __lt__(self, other):
        return self.value > other.value
    def get_value(self):
        if self.count == 1:
            return "Gold Medal"
        elif self.count == 2:
            return "Silver Medal"
        elif self.count == 3:
            return "Bronze Medal"
        else:
            return str(self.count)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nodes = [Node(node) for node in score]
        heapq.heapify(nodes)
        ans = []
        mp = {}
        while len(nodes) > 0:
            n = heapq.heappop(nodes)
            mp[n.value]= n.get_value()
            Node.count += 1
        ans = []
        for el in score:
            ans.append(mp.get(el))
        Node.count = 1
        return ans