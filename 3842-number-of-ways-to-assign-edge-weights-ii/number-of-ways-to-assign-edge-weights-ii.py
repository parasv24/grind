class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = len(edges) + 1
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        parent = [-1] * (n + 1)
        depth = [0] * (n + 1)
        vis = set()
        vis.add(1)
        def dfs(root, p, dep):
            if not root:
                return
            parent[root] = p
            depth[root] = dep + 1
            for child in graph[root]:
                if child not in vis:
                    vis.add(child)
                    dfs(child, root, dep + 1)
            return
        dfs(1, 1, -1)

        logn = ceil(log(n+1, 2))
        lift_table = [[0 for _ in range(n+1)] for _ in range(logn)]
        for i in range(logn):
            for j in range(n+1):
                if i == 0:
                    lift_table[i][j] = parent[j]
                else:
                    lift_table[i][j] = lift_table[i-1][lift_table[i-1][j]]
        
        ans = []
        def get_lca(a, b):
            if a == b:
                return a
            
            i = 0
            while lift_table[i][a] != lift_table[i][b]:
                i += 1
            
            if i == 0:
                return lift_table[i][a]
            return get_lca(lift_table[i-1][a], lift_table[i-1][b])
        MOD = 10 ** 9 + 7
        for x, y in queries:
            depx, depy = depth[x], depth[y]
            if depx > depy:
                x , y = y, x
                depx, depy = depy, depx
            ini_jumps = depy - depx
            binary = bin(ini_jumps)[2:][::-1]
            # print(binary)
            for idx, ch in enumerate(binary):
                if ch == "1":
                    y = lift_table[idx][y]
            # print(x, y)
            lca = get_lca(x, y)
            path_length = depx - depth[lca] + depy - depth[lca]
            # print(path_length, lca, depx, depy)
            if path_length == 0:
                ans.append(0)
            else:
                ans.append(pow(2, path_length-1, MOD))   
        return ans
                
        
        