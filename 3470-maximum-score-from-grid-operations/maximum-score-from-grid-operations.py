class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        # j is the height we select
        n , m = len(grid), len(grid)
        def rec(j, arr):
            if j == m:
                val = 0
                for i in range(n):
                    for k in range(m):
                        if i >= arr[k]:
                            if (k > 0 and i < arr[k - 1]) or (k < m - 1 and i < arr[k + 1]):
                                val += grid[i][k]
                return val
            
            ans = -1
            for i in range(n+1):
                arr[j] = i
                ans = max(ans, rec(j+1, arr))
            return ans
        # return rec(0, [0] * m)

        psum = [[0 for _ in range(n+1)] for _ in range(n)]
        for j in range(n):              # column
            for i in range(n):          # row
                psum[j][i+1] = psum[j][i] + grid[i][j]
        
        @cache
        def rec(taken, h, col):
            if col == n:
                return 0

            maxi = 0

            for height in range(0, n+1):
                prev = 0
                cur = 0

                # prevColScore (left boundary)
                if (not taken) and col-1 >= 0 and height > h:
                    prev = psum[col-1][height] - psum[col-1][h]

                # currColScore (right boundary)
                if h > height:
                    cur = psum[col][h] - psum[col][height]

                # DO NOT overwrite `taken`
                tk = cur + prev + rec(True, height, col+1)
                not_taken = prev + rec(False, height, col+1)

                maxi = max(maxi, tk, not_taken)

            return maxi

        return rec(False, 0, 0)