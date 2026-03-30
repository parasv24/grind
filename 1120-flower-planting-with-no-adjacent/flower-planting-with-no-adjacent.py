class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for i , j in paths:
            adj_list[i-1].append(j-1)
            adj_list[j-1].append(i-1)
        
        colors = [i+1 for i in range(4)]
        ans = [-1 for _ in range(n)]
        
        def rec(i):
            if i == n:
                return True
            
            for color in colors:
                flag = True
                for neighbor in adj_list[i]:
                    if ans[neighbor] == color:
                        flag = False
                if flag:
                    ans[i] = color
                    val = rec(i+1)
                    if val == True:
                        return val
                    ans[i] = -1
            return False
        
        val = rec(0)
        # print(ans)
        return ans
        