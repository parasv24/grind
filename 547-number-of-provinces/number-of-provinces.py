class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        comps = 0
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and isConnected[i][j] == 1:
                    dfs(j)
            return
        for i in range(n):
            if not visited[i]:
                dfs(i)
                comps += 1
        return comps