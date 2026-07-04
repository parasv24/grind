from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        q = deque([1])
        ans = float('inf')

        while q:
            node = q.popleft()

            if node in visited:
                continue

            visited.add(node)

            for nei, weight in graph[node]:
                ans = min(ans, weight)   # consider edge in this component
                if nei not in visited:
                    q.append(nei)

        return ans