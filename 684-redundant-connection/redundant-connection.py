class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if size[px] < size[py]:
                px, py = py, px
            
            parent[py] = px
            size[px] += size[py]
            return True
        
        for x, y in edges:
            val = union(x, y)
            if val == False:
                return [x, y]
        
        