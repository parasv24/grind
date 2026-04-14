class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # def rec(i):
        #     if i == len(robot):
        #         return 0
        #     ans = 10 ** 12
        #     for j in range(len(factory)):
        #         if factory[j][1] > 0:
        #             factory[j][1] -= 1
        #             ans = min(ans, abs(robot[i] - factory[j][0]) + rec(i+1))
        #             factory[j][1] += 1
        #     return ans
        # return rec(0)

        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        @lru_cache(None)
        def dp(i, j):
            # all robots assigned
            if i == n:
                return 0
            
            # no factories left but robots remain
            if j == m:
                return float('inf')
            
            # option 1: skip factory
            res = dp(i, j + 1)
            
            pos, cap = factory[j]
            cost = 0
            
            # option 2: assign k robots
            for k in range(1, cap + 1):
                if i + k > n:
                    break
                
                cost += abs(robot[i + k - 1] - pos)
                
                res = min(
                    res,
                    cost + dp(i + k, j + 1)
                )
            
            return res
        
        return dp(0, 0)

        