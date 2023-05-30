class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def f(n):
        #     if n >= len(cost):
        #         return 0
        #     return cost[n] + min(f(n+1),f(n+2))
        # return min(f(0), f(1))
        
        dp = [-1 for _ in range(len(cost)+1)]
        # def m(n):
        #     if n >= len(cost):
        #         return 0
        #     if dp[n]!= -1:
        #         return dp[n]
        #     dp[n] = cost[n] + min(m(n+1),m(n+2))
        #     return dp[n]
        # return min(m(0), m(1))
        
        # TABULATION
        
        n = len(cost)
        for i in range(n-1, -1, -1):
            dp[i] = cost[i]
            x = y = 0
            if i + 1 < n:
                x = dp[i+1]
            if i + 2 < n:
                y = dp[i+2]
            
            dp[i] += min(x,y)
        return min(dp[0], dp[1])
            
            
