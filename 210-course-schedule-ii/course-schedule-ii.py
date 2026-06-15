class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[y].append(x)
    
        vis = [0] * numCourses
        order = []
        def dfs(i):
            vis[i] = 1
            for neighbor in graph[i]:
                if vis[neighbor] == 1:
                    return True
                if vis[neighbor] == 0 and dfs(neighbor):
                    return True
            vis[i] = 2
            order.append(i)
            return False
        
        for i in range(numCourses):
            if vis[i] == 0:
                has_cycle = dfs(i)
                if has_cycle:
                    return []
        return order[::-1]
        
            

        