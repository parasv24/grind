
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nodes = [-1 * node for node in piles]
        heapify(nodes)
        while(k > 0):
            val = nodes[0]//2
            heapreplace(nodes, val)
            k -= 1
        total = sum(nodes)
        return -1 * total
        