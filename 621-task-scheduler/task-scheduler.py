class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        max_heap = []
        for key , value in mp.items():
            heapq.heappush(max_heap, (-value, key))
        
        deq = deque()
        time = 0
        while max_heap or deq:
            time += 1

            if max_heap:
                freq, val = heapq.heappop(max_heap)
                if freq + 1 < 0:
                    deq.append((freq + 1, val, time + n))
            if deq and deq[0][2] == time:
                prev = deq.popleft()
                heapq.heappush(max_heap,(prev[0], prev[1]))
        return time
                