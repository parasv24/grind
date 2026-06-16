class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        dist = [[10**9] * cols for _ in range(rows)]
        dist[0][0] = 0
        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while heap:
            effort, i, j = heapq.heappop(heap)
            if effort > dist[i][j]:
                continue
            if i == rows - 1 and j == cols - 1:   # optional early exit
                return effort
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[nx][ny] - heights[i][j]))
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))
        return dist[-1][-1]