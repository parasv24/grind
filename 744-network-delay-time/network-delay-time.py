class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = []
        heap.append((0,k))
        times = [100000] * (n+1)
        times[k] = 0
        while heap:
            time, node = heapq.heappop(heap)
            
            # stale entry needs to be lazy skipped
            if time > times[node]:
                continue
            
            for neighbor, t in graph[node]:
                if time + t < times[neighbor]:
                    times[neighbor] = time + t
                    heapq.heappush(heap, (time + t, neighbor))
        
        mini = max(times[1:]) 
        return mini if mini != 100000 else -1
