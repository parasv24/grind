class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        adj = [[0] * n for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            adj[x][y] = 1
            adj[y][x] = 1
        vis = set()
        ans = 0
        for i in range(n):
            if i not in vis:
                component = []
                queue = deque()
                queue = [i]
                vis.add(i)
                while queue:
                    node = queue.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in vis:
                            vis.add(neighbor)
                            queue.append(neighbor)
                valid = True
                # print(component)
                for j in range(len(component)):
                    for k in range(j+1, len(component)):
                        if adj[component[j]][component[k]] == 0:
                            valid = False
                            break
                ans += valid
        return ans
                    


        