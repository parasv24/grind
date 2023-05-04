class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        n = len(image)
        m = len(image[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        init_color = image[sr][sc]
        delr = [ -1 , 0 , 0, 1]
        delc = [ 0 , -1, 1, 0]
        def dfs(sr, sc, init_color):
            vis[sr][sc] = 1
            for i in range(0,4):
                nr = sr + delr[i]
                nc = sc + delc[i]
                if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and image[nr][nc] == init_color:
                    dfs(nr, nc, init_color)
        dfs(sr,sc, init_color)
        for i in range(0, n):
            for j in range(0, m):
                if vis[i][j] == 1:
                    image[i][j] = color
        return image
