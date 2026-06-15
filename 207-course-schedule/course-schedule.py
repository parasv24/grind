class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        graph = defaultdict(list)
        def dfs(i):
            visited[i] = 1
            for child in graph[i]:
                if visited[child] == 1:
                    return True
                if visited[child] == 0 and dfs(child):
                    return True
            visited[i] = 2
            return False
        
        for u, v in prerequisites:
            graph[v].append(u)

        for i in range(numCourses):
            if visited[i] == 0:
                has_cycle = dfs(i)
                if has_cycle:
                    return False
        return True

        