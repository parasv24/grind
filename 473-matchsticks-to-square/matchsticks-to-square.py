class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sm = sum(matchsticks)
        val = sm // 4
        if sm % 4 != 0:
            return False
        mx = max(matchsticks)
        if mx > val:
            return False
        @cache
        def dfs(mask, cur_sum, cur):
            if cur == 3:
                return True
            
            if cur_sum == val:
                return dfs(mask , 0, cur + 1)
            
            for i in range(len(matchsticks)):
                if (1 << i) & mask == 0:
                    if cur_sum + matchsticks[i] > val:
                        return False
                    if dfs(mask | (1 << i), cur_sum + matchsticks[i], cur):
                        return True
            return False
        return dfs(0, 0, 0)
        
                       

            


        