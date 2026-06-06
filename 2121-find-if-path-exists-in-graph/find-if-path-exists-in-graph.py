class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if size[px] < size[py]:
                py, px = px, py
            
            parent[py] = px
            size[px] += size[py]
            return True

        for x, y in edges:
            union(x, y)
        
        return find(source) == find(destination)