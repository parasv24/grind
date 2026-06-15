class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m , n = len(image), len(image[0])
        oc = image[sr][sc]
        image[sr][sc] = color
        stack = [(sr, sc)]
        vis = set([(sr, sc)])
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            sr, sc = stack.pop()
            for dx, dy in delta:
                nr, nc = sr + dx, sc + dy
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == oc and (nr, nc) not in vis:
                    image[nr][nc] = color
                    stack.append((nr, nc))
                    vis.add((nr, nc))
        return image