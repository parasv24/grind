class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = [-1] * len(graph)
        def dfs(node, color):
            vis[node] = color
            for n in graph[node]:
                if vis[n] == -1:
                    if dfs(n, (color + 1 ) % 2) == False:
                        return False
                elif vis[n] == color:
                    return False
            return True
        for i in range(len(graph)):
            if vis[i] == -1:
                if dfs(i, 0) == False:
                    return False
        return True
