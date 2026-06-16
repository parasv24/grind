class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, w in flights:
            graph[x].append((y, w))

        heap = [(0, src, 0)]
        costs = [[10 ** 6 for _ in range(k+3)] for _ in range(n)]
        costs[src][0] = 0
        while heap:
            cost, node, stops = heapq.heappop(heap)

            if cost > costs[node][stops]:
                continue
            
            for neighbor, c in graph[node]:
                if cost + c < costs[neighbor][stops+1] and stops <= k:
                    costs[neighbor][stops+1] = cost+c
                    heapq.heappush(heap, (cost+c, neighbor, stops+1))
        ans = min(costs[dst])
        return ans if ans != 10 ** 6 else -1        