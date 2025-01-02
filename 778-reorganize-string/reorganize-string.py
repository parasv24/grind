class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(list(s))
        max_heap = []
        for char, freq in mp.items():
            heappush(max_heap, (-freq, char))
    
        result = []
        prev_char, prev_freq = None, 0 
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_char and prev_freq !=0 and prev_char != char:
                heappush(max_heap, (prev_freq, prev_char))
            
            prev_char, prev_freq = char, freq + 1
        rs_string = "".join(result)
        return rs_string if len("".join(result)) == len(s) else ""
        