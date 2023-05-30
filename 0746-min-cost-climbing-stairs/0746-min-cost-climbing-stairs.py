class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def f(n):
            if n >= len(cost):
                return 0
            return cost[n] + min(f(n+1),f(n+2))
        # return min(f(0), f(1))
        
        dp = [-1 for _ in range(len(cost)+1)]
        def m(n):
            if n >= len(cost):
                return 0
            if dp[n]!= -1:
                return dp[n]
            dp[n] = cost[n] + min(m(n+1),m(n+2))
            return dp[n]
        return min(m(0), m(1))
            
