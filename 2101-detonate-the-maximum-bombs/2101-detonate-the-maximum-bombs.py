class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = []
        n = len(bombs)
        
        for i in range(n):
            x,y,r = bombs[i]
            adj.append([])
            for j in range(n):
                if i == j:
                    continue
                x1, y1, _ = bombs[j]
                if r ** 2 >= (x-x1)**2 + (y-y1) ** 2:
                    adj[i].append(j)
                    
        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for j in adj[i]:
                if j not in seen:
                    dfs(j)
        
        maxi = -1
        # print(adj)
        for i in range(len(bombs)):
            seen = set()
            dfs(i)
            maxi = max(maxi, len(seen))
        return maxi
        