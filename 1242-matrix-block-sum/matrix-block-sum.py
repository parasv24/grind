class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        p_sum = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1, m+1):
                p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + mat[i-1][j-1]
        
        ans = [[0] * m for _ in range(n)]
        #print(p_sum)
        for i in range(n):
            for j in range(m):
                r1 = max(0, i - k) + 1
                r2 = min(n-1, i + k) + 1
                c1 = max(0 , j - k) + 1
                c2 = min(m-1, j + k) + 1
                ans[i][j] = p_sum[r2][c2] - p_sum[r2][c1-1] - p_sum[r1-1][c2] + p_sum[r1-1][c1-1]
        return ans
        