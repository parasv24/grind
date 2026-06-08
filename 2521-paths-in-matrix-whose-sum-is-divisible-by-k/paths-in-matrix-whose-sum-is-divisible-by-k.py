class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        # @cache
        # def rec(i, j, sm):
        #     if i == n-1 and j == m-1:
        #         sm += grid[i][j]
        #         return int(sm % k == 0)
        #     ans = 0
        #     val = grid[i][j]
        #     if i + 1 < n:
        #         ans += rec(i+1, j, (sm + val) % k)
        #     if j + 1 < m:
        #         ans += rec(i, j+1, (sm + val) % k)
        #     return ans % (10 ** 9 + 7)
        # return rec(0, 0, 0)

        prev = [[0] * k for _ in range(m)]

        for i in range(n):

            curr = [[0] * k for _ in range(m)]

            for j in range(m):

                if i == 0 and j == 0:
                    curr[0][grid[0][0] % k] = 1
                    continue

                val = grid[i][j]

                for rem in range(k):

                    new_rem = (rem + val) % k

                    # top
                    if i > 0:
                        curr[j][new_rem] += prev[j][rem]

                    # left
                    if j > 0:
                        curr[j][new_rem] += curr[j-1][rem]
                    
                    curr[j][new_rem] = curr[j][new_rem] % (10 ** 9 + 7)
            prev = curr
        return prev[-1][0]


            
        