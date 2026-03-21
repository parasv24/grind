class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        courses = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)
            courses[x] += 1
        queue = deque([i for i in range(numCourses) if courses[i] == 0])
        leng = 0
        while len(queue) > 0:
            node = queue.popleft()
            leng += 1
            for i in graph[node]:
                courses[i] -= 1
                if courses[i] == 0:
                    queue.append(i)
        if leng == numCourses:
            return True
        return False 

        