class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dis = []
        for i in range(n):
            for j in range(i+1, n):
                xi, xj = points[i]
                yi, yj = points[j]
                dis.append((abs(xi-yi) + abs(xj-yj), i, j))
        dis.sort()
        
        count = 0
        total = 0

        parent = list(range(n))
        rank = [0] * n
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            ru, rv = rank[pu], rank[pv]

            if pu == pv:
                return False
            
            if ru < rv:
                ru, rv = rv, ru
                pu, pv = pv, pu
            
            parent[pv] = pu
            if ru == rv:
                rank[pv] += 1
            return True
        
        for d, src, dest in dis:
            if union(src, dest):
                total += d
                count += 1

                if count == n-1:
                    return total
        return 0