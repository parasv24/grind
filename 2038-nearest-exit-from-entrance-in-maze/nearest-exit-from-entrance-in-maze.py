class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[maze[i][j] == "+" for j in range(len(maze[0]))] for i in range(0, len(maze))] 
        queue = []
        i , j = entrance
        visited[i][j] = True
        queue.append([i , j, 0])
        diff = [[0,1], [0 , -1], [1, 0], [-1, 0]]
        while len(queue) > 0:
            xi, xj , ans = queue[0]
            queue.pop(0)
            if (xi == 0 or xi == len(maze) - 1 or xj == 0 or xj == len(maze[0]) - 1) and (xi != i or xj != j):
                return ans
            for i , j in diff:
                if 0<= xi + i < len(maze) and 0 <= xj + j < len(maze[0]) and not visited[xi+i][xj + j]:
                    queue.append([xi + i, xj + j, ans + 1])
                    visited[xi+i][xj + j] = True
        return -1
        
        