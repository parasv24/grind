from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        sr = sc = -1
        total_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    sr, sc = i, j
                if "a" <= grid[i][j] <= "z":
                    total_keys += 1

        all_keys = (1 << total_keys) - 1
        queue = deque([(sr, sc, 0, 0)])      # (row, col, keys, steps)
        vis = {(sr, sc, 0)}                   # ✅ state includes the key mask
        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            i, j, mask, steps = queue.popleft()
            if mask == all_keys:
                return steps
            for dx, dy in delta:
                ni, nj = i + dx, j + dy
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                cell = grid[ni][nj]
                if cell == "#":
                    continue                  # wall
                if "A" <= cell <= "Z" and not (mask & (1 << (ord(cell) - ord("A")))):
                    continue                  # locked, no key
                new_mask = mask
                if "a" <= cell <= "z":
                    new_mask |= (1 << (ord(cell) - ord("a")))   # pick up key
                if (ni, nj, new_mask) not in vis:   # ✅ visited on the FULL state
                    vis.add((ni, nj, new_mask))
                    queue.append((ni, nj, new_mask, steps + 1))
        return -1