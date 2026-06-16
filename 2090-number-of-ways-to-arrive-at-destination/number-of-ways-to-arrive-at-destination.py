class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ways = [0] * n
        dist = [10**12] * n
        dist[0] = 0
        ways[0] = 1
        graph = defaultdict(list)
        
        for x, y , w in roads:
            graph[x].append((y, w))
            graph[y].append((x, w))
        
        heap = [(0, 0)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue
            
            for neighbor, t in graph[node]:
                if time + t == dist[neighbor]:
                    ways[neighbor] += ways[node]
                if time + t < dist[neighbor]:
                    ways[neighbor] = ways[node]
                    dist[neighbor] = time + t
                    heapq.heappush(heap,(time + t, neighbor))
        return ways[-1] % (10 ** 9 + 7)
                