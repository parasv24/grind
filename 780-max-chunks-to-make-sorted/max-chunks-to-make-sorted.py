class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_till_now = -1
        for idx, el in enumerate(arr):
            max_till_now = max(max_till_now, el)
            if max_till_now == idx:
                chunks += 1
        return chunks
        