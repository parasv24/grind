class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        gs = {}
        for i in range(n):
            gs[i]= []
        for x,y in edges:
            gs[x].append(y)
            gs[y].append(x)
        vis = [False] * n
        vis[source] = True
        queue = [source]
        print(queue)
        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            for n in gs[node]:
                if not vis[n]:
                    vis[n] = True
                    queue.append(n)
        return vis[destination]
        