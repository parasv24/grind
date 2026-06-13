class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 2

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        qmp = defaultdict(list)
        depth = [0] * n
        for i in range(len(queries)):
            x, y = queries[i]
            qmp[x].append((y, i))
            qmp[y].append((x, i))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj
        
        parent = [i for i in range(n)]
        
        color = [0] * n
        ans = [0] * len(queries)
        def dfs(root, dep):
            color[root] = 1
            depth[root] = dep
            for child in graph[root]:
                if not color[child]:
                    dfs(child, dep+1)
                    union(child, root)
            
            for other_root, idx in qmp[root]:
                if color[other_root] == 2:
                    lca = find(other_root)
                    length = depth[root] + depth[other_root] - (2 * depth[lca])
                    ans[idx] = pow(2, length-1, MOD)
            color[root] = 2
        dfs(1, 0)
        return ans 





                
        
        