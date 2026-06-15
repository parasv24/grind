class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.pop()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
            

        