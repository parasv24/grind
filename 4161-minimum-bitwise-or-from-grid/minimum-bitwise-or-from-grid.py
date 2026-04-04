class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:

        # T.L.E
        n , m = len(grid), len(grid[0])

        # dp = [set() for i in range(n)]
        # dp[0] = set(grid[0])

        # for i in range(1, n):
        #     for j in range(0, m):
        #         for el in dp[i-1]:
        #             dp[i].add(el | grid[i][j])

        # return min(dp[n-1])
        
        @cache
        def rec(i, j, cur):
            if i == n:
                return cur
            ans = 1000000
            for j in range(m):
                ans = min(ans, rec(i+1, cur | grid[i][j]))
            return ans
        # return rec(0, 0)

        #Greedy solution try to form a number with bits off 

        ans = 0

        for bit in range(17, -1, -1):
            temp = [[] for _ in range(n)]
            possible = True

            for i in range(n):
                for el in grid[i]:
                    if el & (1 << bit) == 0:
                        temp[i].append(el) 
                if not temp[i]:
                    possible = False
                    break
            
            if not possible:
                ans |= (1 << bit)
            else:
                grid = temp
        return ans

        

            
        
        