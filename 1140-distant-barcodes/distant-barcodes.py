class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        mp = Counter(barcodes)
        max_heap = []
        for char, freq in mp.items():
            heappush(max_heap, (-freq, char))
    
        result = []
        prev_char, prev_freq = None, 0 
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_char and prev_freq !=0:
                heappush(max_heap, (prev_freq, prev_char))
            
            prev_char, prev_freq = char, freq + 1
        return result 
        