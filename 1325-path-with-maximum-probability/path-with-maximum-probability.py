class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        heap = [(-1, start_node)]
        muls = [0] * n
        muls[start_node] = 1
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -1 * prob
            if prob < muls[node]:
                continue
            
            for neighbor, w in graph[node]:
                if prob * w > muls[neighbor]:
                    muls[neighbor] = prob * w
                    heapq.heappush(heap, (-(prob*w), neighbor))
        
        return muls[end_node]
