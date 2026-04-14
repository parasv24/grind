class Node:
    def __init__(self, freq, val):
        self.freq = freq
        self.val = val
    def __lt__(self, oth):
        if self.freq == oth.freq:
            return self.val > oth.val
        return self.freq < oth.freq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        ans = []
        for key,v in mp.items():
            heappush(ans, Node(v, key))
            if len(ans) > k:
                heappop(ans)
        ans.sort(key=lambda x: (-x.freq, x.val))
        return [node.val for node in ans]
        