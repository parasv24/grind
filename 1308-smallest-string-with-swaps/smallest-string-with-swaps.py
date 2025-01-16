class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # if len(pairs) == 0:
        #     return s
        n = len(s)
        mp = {}
        for x, y in pairs:
            if mp.get(x, False) == False:
                mp[x] = [y]
            else:
                mp[x].append(y)
            
            if mp.get(y, False) == False:
                mp[y] = [x]
            else:
                mp[y].append(x)
        
        vis = [0] * n
        st = [-1] * n
        def dfs(idx,c):
            vis[idx] = 1
            st[idx] = c
            output = [s[idx]]
            for el in mp[idx]:
                if vis[el] == 0:
                    output += dfs(el,c)
            return output
        color = 0
        ans = {}
        for i in range(n):
            if mp.get(i, False) == False:
                ans[color] = [s[i]]
                st[i] = color
            elif vis[i] == 0: 
                ans[color] = sorted(dfs(i, color))
            color += 1
        output = []
        for i in range(n):
            output.append(ans[st[i]][0])
            ans[st[i]].pop(0)
        return "".join(output)


            
        
        