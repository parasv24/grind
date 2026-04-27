class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n , m = len(grid), len(grid[0])
        mp = {
            1: [[1, 4, 6], [1, 3, 5], [], []],
            2: [[], [], [2, 3, 4], [2,5,6]],
            3: [[4, 6, 1], [], [], [5, 6, 2]],
            4: [[], [1, 3, 5], [], [2,5,6]],
            5: [[1, 4, 5], [], [2, 3, 4], []],
            6: [[], [1, 3, 5], [2, 3, 4], []]
        }
        queue = deque()
        vis = set()
        queue.append((0, 0))
        vis.add((0, 0))
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            x, y = queue.popleft()
            # print(x, y, grid[x][y])
            if x == n-1 and y == m-1:
                return True
            for idx, arr in enumerate(delta):
                dx, dy = arr
                nx, ny = x + dy, y + dx
                # print("nx", nx, ny, mp[grid[x][y]][idx], idx)
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis and grid[nx][ny] in mp[grid[x][y]][idx]:
                    vis.add((nx, ny))
                    queue.append((nx, ny))
        return False



        