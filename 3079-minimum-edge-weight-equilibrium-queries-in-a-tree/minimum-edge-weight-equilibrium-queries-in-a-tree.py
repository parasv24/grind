class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = [0] * n
        depth = [0] * n
        logn = int(log(n, 2))+1
        mp2 = {}
        mp = defaultdict(list)
        for x, y, w in edges:
            mp[x].append((y, w))
            mp[y].append((x, w))
            mp2[(x,y)] = w
            mp2[(y,x)] = w
        
        
        def dfs(root, p, dep):
            parent[root] = p
            depth[root] = dep
            for child, _ in mp[root]:
                if child != p:
                    dfs(child, root, dep + 1)
            return
        dfs(0, 0, 0)
        lift_table = [[[0, [0] * 27] for _ in range(n)] for _ in range(logn)]
        # print(parent, depth)
        for i in range(logn):
            for j in range(n):
                if i == 0:
                    if j != 0:
                        lift_table[i][j][0] = parent[j]
                        lift_table[i][j][1][mp2[(j, parent[j])]] = 1
                else:
                    lift_table[i][j][0] = lift_table[i-1][lift_table[i-1][j][0]][0]
                    for k in range(27):
                        lift_table[i][j][1][k] = lift_table[i-1][j][1][k] + lift_table[i-1][lift_table[i-1][j][0]][1][k]
        
        ans = []
        for x, y in queries:
            cx, cy = x, y
            dx, dy = depth[x], depth[y]
            if dx > dy:
                x, y = y, x
                cx, cy = cy, cx
                dx, dy = dy, dx
            
            diff = dy - dx
            vals = [0] * 27
            for i in range(logn):
                if diff & (1 << i):
                    cy = lift_table[i][cy][0]
            if cx == cy:
                lca = cx
            else:
                for i in range(logn-1, -1, -1):
                    if lift_table[i][cx][0] != lift_table[i][cy][0]:
                        cx = lift_table[i][cx][0]
                        cy = lift_table[i][cy][0]
                lca = parent[cx]
            
            dx = depth[x] - depth[lca]
            for i in range(logn):
                if dx & (1 << i):
                    for k in range(27):
                        vals[k] += lift_table[i][x][1][k]
                    x = lift_table[i][x][0]

            # collect path y -> lca
            dy = depth[y] - depth[lca]
            for i in range(logn):
                if dy & (1 << i):
                    for k in range(27):
                        vals[k] += lift_table[i][y][1][k]
                    y = lift_table[i][y][0]
            # print(vals)
            ans.append(sum(vals)- max(vals))
        
        return ans





