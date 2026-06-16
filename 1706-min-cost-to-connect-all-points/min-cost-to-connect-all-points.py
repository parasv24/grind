class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # KRUSKAL
        # dis = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         xi, xj = points[i]
        #         yi, yj = points[j]
        #         dis.append((abs(xi-yi) + abs(xj-yj), i, j))
        # dis.sort()
        
        # count = 0
        # total = 0

        # parent = list(range(n))
        # rank = [0] * n
        
        # def find(i):
        #     if parent[i] != i:
        #         parent[i] = find(parent[i])
        #     return parent[i]
        
        # def union(u, v):
        #     pu, pv = find(u), find(v)
        #     ru, rv = rank[pu], rank[pv]

        #     if pu == pv:
        #         return False
            
        #     if ru < rv:
        #         ru, rv = rv, ru
        #         pu, pv = pv, pu
            
        #     parent[pv] = pu
        #     if ru == rv:
        #         rank[pu] += 1
        #     return True
        
        # for d, src, dest in dis:
        #     if union(src, dest):
        #         total += d
        #         count += 1

        #         if count == n-1:
        #             return total
        # return 0

        # prim's
        n = len(points)
        vis = [False] * n
        heap = [(0, 0)]
        count = 0
        total = 0
        while heap and count < n:
            dis, node = heapq.heappop(heap)
            if vis[node]:
                continue
            
            vis[node] = True
            total += dis
            count += 1

            for j in range(n):
                if node != j:
                    x1, y1 = points[node]
                    x2, y2 = points[j]
                    heapq.heappush(heap, (abs(x1-x2) + abs(y1-y2), j))
        return total

