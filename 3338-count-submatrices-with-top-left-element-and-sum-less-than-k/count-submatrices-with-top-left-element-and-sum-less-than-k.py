class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n , m = len(grid), len(grid[0])
        ans = 0
        for i in range(0, n):
            prev = 0
            for j in range(0, m):
                prev += grid[i][j]
                just_prev = 0 if i == 0 else grid[i-1][j]
                if prev + just_prev <= k:
                    ans += 1
                grid[i][j] = prev + just_prev
        return ans
            
                
                

                