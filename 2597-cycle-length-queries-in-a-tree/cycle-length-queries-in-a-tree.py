class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def get_i_parent(i, x):
            if x == 0:
                return i if i > 0 else 1
            return get_i_parent(i//2, x - 1)
        ans = []
        for x,y in queries:
            depx, depy = int(log(x, 2)), int(log(y, 2))
            if depx > depy:
                y,x = x, y
                depy, depx = depx, depy
            
            diff = depy - depx
            y = get_i_parent(y, diff)
            
            if x == y:
                lca = x
            else:
                for i in range(n-1, -1, -1):
                    if get_i_parent(x, i) != get_i_parent(y, i):
                        x = get_i_parent(x, i)
                        y = get_i_parent(y, i)
                lca = x // 2
                if lca == 0:
                    lca = 1
            level_lca = int(log(lca, 2))
            ans.append(depy - level_lca + depx - level_lca + 1)
        return ans
