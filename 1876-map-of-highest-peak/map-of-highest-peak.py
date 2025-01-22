class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n , m = len(isWater), len(isWater[0])
        graph = [[isWater[i][j] - 1 for j in range(m)] for i in range(n)]
        delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    queue.append([i, j])
        lvl_value = 1
        while queue:
            len_level = len(queue)
            for i in range(len_level):
                i, j = queue.pop(0)
                val = graph[i][j]
                for x, y in delta:
                    if 0 <= i + x <= n-1 and 0 <= j + y <= m-1 and graph[i+x][j+y]== -1:
                        graph[i+x][j+y] = lvl_value
                        queue.append([i+x, y+j])
            lvl_value += 1
        return graph
                        

        