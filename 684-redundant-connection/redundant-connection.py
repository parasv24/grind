class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            px, py = find(u), find(v)

            if px == py:
                return False

            if rank[px] < rank[py]:
                py, px = px, py
            
            parent[py] = px

            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        for x, y in edges:
            if union(x, y) == False:
                return [x, y]
        
            
        
        